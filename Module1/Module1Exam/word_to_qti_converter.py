#!/usr/bin/env python3
import docx
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import zipfile
import hashlib
from datetime import datetime
import sys

class WordToQTIConverter:
    def __init__(self):
        self.questions = []
        self.quiz_title = ""

    def parse_word_doc(self, doc_path):
        doc = docx.Document(doc_path)
        self.quiz_title = os.path.splitext(os.path.basename(doc_path))[0]

        current_question = None
        current_choices = []
        correct_answer = None

        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue

            question_match = re.match(r'^(\d+)\.\s+(.+)', text)
            if question_match:
                if current_question:
                    self.questions.append({
                        'question': current_question,
                        'choices': current_choices,
                        'correct': correct_answer,
                        'type': 'multiple_choice'
                    })

                current_question = question_match.group(2)
                current_choices = []
                correct_answer = None
                continue

            choice_match = re.match(r'^([a-eA-E])\)\s*(.+)', text)
            if choice_match:
                choice_letter = choice_match.group(1).upper()
                choice_text = choice_match.group(2)

                is_correct = False
                if '*' in choice_text or '(correct)' in choice_text.lower():
                    is_correct = True
                    correct_answer = len(current_choices)
                    choice_text = re.sub(r'\*|\s*\(correct\)\s*', '', choice_text, flags=re.IGNORECASE).strip()

                current_choices.append({
                    'text': choice_text,
                    'correct': is_correct
                })
                continue

            answer_match = re.match(r'^Answer:\s*([a-eA-E])', text, re.IGNORECASE)
            if answer_match:
                answer_letter = answer_match.group(1).upper()
                answer_index = ord(answer_letter) - ord('A')
                if 0 <= answer_index < len(current_choices):
                    for i, choice in enumerate(current_choices):
                        choice['correct'] = (i == answer_index)
                    correct_answer = answer_index

        if current_question:
            self.questions.append({
                'question': current_question,
                'choices': current_choices,
                'correct': correct_answer,
                'type': 'multiple_choice'
            })

    def create_qti_assessment(self):
        assessment = ET.Element('assessment', {
            'xmlns': 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2',
            'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xsi:schemaLocation': 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd',
            'ident': f'assessment_{hashlib.md5(self.quiz_title.encode()).hexdigest()[:8]}',
            'title': self.quiz_title
        })

        qtimetadata = ET.SubElement(assessment, 'qtimetadata')

        qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(qtimetadatafield, 'fieldlabel').text = 'cc_maxattempts'
        ET.SubElement(qtimetadatafield, 'fieldentry').text = '1'

        section = ET.SubElement(assessment, 'section', {'ident': 'root_section'})

        for idx, q in enumerate(self.questions, 1):
            item = ET.SubElement(section, 'item', {
                'ident': f'question_{idx}_{hashlib.md5(q["question"].encode()).hexdigest()[:8]}',
                'title': f'Question {idx}'
            })

            itemmetadata = ET.SubElement(item, 'itemmetadata')
            qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')

            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            ET.SubElement(qtimetadatafield, 'fieldlabel').text = 'question_type'
            ET.SubElement(qtimetadatafield, 'fieldentry').text = 'multiple_choice_question'

            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            ET.SubElement(qtimetadatafield, 'fieldlabel').text = 'points_possible'
            ET.SubElement(qtimetadatafield, 'fieldentry').text = '1.0'

            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            ET.SubElement(qtimetadatafield, 'fieldlabel').text = 'original_answer_ids'
            ET.SubElement(qtimetadatafield, 'fieldentry').text = ','.join([str(i) for i in range(len(q['choices']))])

            qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
            ET.SubElement(qtimetadatafield, 'fieldlabel').text = 'assessment_question_identifierref'
            ET.SubElement(qtimetadatafield, 'fieldentry').text = f'question_{idx}'

            presentation = ET.SubElement(item, 'presentation')

            material = ET.SubElement(presentation, 'material')
            mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/html'})
            mattext.text = f'<p>{q["question"]}</p>'

            response_lid = ET.SubElement(presentation, 'response_lid', {
                'ident': 'response1',
                'rcardinality': 'Single'
            })
            render_choice = ET.SubElement(response_lid, 'render_choice')

            for choice_idx, choice in enumerate(q['choices']):
                response_label = ET.SubElement(render_choice, 'response_label', {
                    'ident': str(choice_idx)
                })
                material = ET.SubElement(response_label, 'material')
                mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/plain'})
                mattext.text = choice['text']

            resprocessing = ET.SubElement(item, 'resprocessing')
            outcomes = ET.SubElement(resprocessing, 'outcomes')
            decvar = ET.SubElement(outcomes, 'decvar', {
                'maxvalue': '100',
                'minvalue': '0',
                'varname': 'SCORE',
                'vartype': 'Decimal'
            })

            for choice_idx, choice in enumerate(q['choices']):
                respcondition = ET.SubElement(resprocessing, 'respcondition', {'continue': 'No'})
                conditionvar = ET.SubElement(respcondition, 'conditionvar')
                varequal = ET.SubElement(conditionvar, 'varequal', {'respident': 'response1'})
                varequal.text = str(choice_idx)
                setvar = ET.SubElement(respcondition, 'setvar', {
                    'action': 'Set',
                    'varname': 'SCORE'
                })
                setvar.text = '100' if choice['correct'] else '0'
                if choice['correct']:
                    displayfeedback = ET.SubElement(respcondition, 'displayfeedback', {
                        'feedbacktype': 'Response',
                        'linkrefid': 'correct_fb'
                    })
                else:
                    displayfeedback = ET.SubElement(respcondition, 'displayfeedback', {
                        'feedbacktype': 'Response',
                        'linkrefid': 'general_fb'
                    })

            itemfeedback_correct = ET.SubElement(item, 'itemfeedback', {'ident': 'correct_fb'})
            flow_mat = ET.SubElement(itemfeedback_correct, 'flow_mat')
            material = ET.SubElement(flow_mat, 'material')
            mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/html'})
            mattext.text = '<p>Correct!</p>'

            itemfeedback_general = ET.SubElement(item, 'itemfeedback', {'ident': 'general_fb'})
            flow_mat = ET.SubElement(itemfeedback_general, 'flow_mat')
            material = ET.SubElement(flow_mat, 'material')
            mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/html'})
            mattext.text = '<p>Incorrect.</p>'

        return assessment

    def create_manifest(self, assessment_files):
        manifest = ET.Element('manifest', {
            'xmlns': 'http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1',
            'xmlns:lom': 'http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource',
            'xmlns:imsmd': 'http://www.imsglobal.org/xsd/imsmd_v1p2',
            'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'identifier': 'qti_export_manifest',
            'xsi:schemaLocation': 'http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p1.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://www.imsglobal.org/xsd/imsmd_v1p2 http://www.imsglobal.org/xsd/imsmd_v1p2p2.xsd'
        })

        metadata = ET.SubElement(manifest, 'metadata')
        schema = ET.SubElement(metadata, 'schema')
        schema.text = 'IMS Content'
        schemaversion = ET.SubElement(metadata, 'schemaversion')
        schemaversion.text = '1.1.3'

        imsmd_lom = ET.SubElement(metadata, '{http://www.imsglobal.org/xsd/imsmd_v1p2}lom')
        imsmd_general = ET.SubElement(imsmd_lom, '{http://www.imsglobal.org/xsd/imsmd_v1p2}general')
        imsmd_title = ET.SubElement(imsmd_general, '{http://www.imsglobal.org/xsd/imsmd_v1p2}title')
        imsmd_langstring = ET.SubElement(imsmd_title, '{http://www.imsglobal.org/xsd/imsmd_v1p2}langstring')
        imsmd_langstring.text = 'QTI Assessment Export'

        organizations = ET.SubElement(manifest, 'organizations')

        resources = ET.SubElement(manifest, 'resources')

        for assessment_file in assessment_files:
            resource = ET.SubElement(resources, 'resource', {
                'identifier': assessment_file.replace('.xml', ''),
                'type': 'imsqti_xmlv1p2',
                'href': assessment_file
            })
            file_elem = ET.SubElement(resource, 'file', {'href': assessment_file})

            dependency = ET.SubElement(resource, 'dependency', {
                'identifierref': 'QTI_Dependencies'
            })

        return manifest

    def prettify(self, elem):
        rough_string = ET.tostring(elem, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def save_xml(self, element, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.prettify(element))

def main():
    converter = WordToQTIConverter()

    word_docs = [f for f in os.listdir('.') if f.endswith('.docx')]

    if not word_docs:
        print("No Word documents found in current directory")
        return

    assessment_files = []

    if not os.path.exists('qti_output'):
        os.makedirs('qti_output')

    for doc_file in word_docs:
        print(f"Processing: {doc_file}")
        converter.questions = []
        converter.parse_word_doc(doc_file)

        if converter.questions:
            print(f"  Found {len(converter.questions)} questions")
            assessment = converter.create_qti_assessment()

            output_filename = doc_file.replace('.docx', '.xml')
            output_path = f'qti_output/{output_filename}'
            converter.save_xml(assessment, output_path)
            assessment_files.append(output_filename)
            print(f"  Saved to: {output_path}")
        else:
            print(f"  No questions found in {doc_file}")

    if assessment_files:
        manifest = converter.create_manifest(assessment_files)
        converter.save_xml(manifest, 'qti_output/imsmanifest.xml')

        zip_filename = 'canvas_qti_export.zip'
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for root, dirs, files in os.walk('qti_output'):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, 'qti_output')
                    zipf.write(file_path, arcname)

        print(f"\n✓ QTI export created: {zip_filename}")
        print(f"  Total assessments: {len(assessment_files)}")
        print("\nTo import to Canvas:")
        print("  1. Go to your Canvas course")
        print("  2. Navigate to Settings → Import Course Content")
        print("  3. Choose 'QTI .zip file' as the content type")
        print("  4. Upload the canvas_qti_export.zip file")

if __name__ == "__main__":
    main()
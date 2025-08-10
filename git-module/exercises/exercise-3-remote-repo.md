# Exercise 3: Working with Remote Repositories

## Objective
Connect your local repository to a remote hosting service (GitHub) and sync changes.

## Prerequisites
- GitHub account created
- Local repository from previous exercises

## Steps

1. **Create a new repository on GitHub**
   - Go to github.com and click "New repository"
   - Name it "csci101-git-practice"
   - Don't initialize with README (your local repo already has files)
   - Copy the repository URL

2. **Connect local repo to remote**
   ```bash
   git remote add origin https://github.com/yourusername/csci101-git-practice.git
   ```

3. **Push your commits to GitHub**
   ```bash
   git push -u origin main
   ```
   (Note: Use `master` instead of `main` if that's your default branch)

4. **Make a change locally**
   ```bash
   echo "Remote repositories enable collaboration." >> notes.txt
   git add notes.txt
   git commit -m "Add note about collaboration"
   ```

5. **Push the new commit**
   ```bash
   git push
   ```

6. **View your repository on GitHub**
   - Refresh your GitHub repository page
   - Browse the files and commit history

## Questions
- What does `origin` represent?
- What's the difference between the first `git push -u origin main` and subsequent `git push` commands?
- How does the web interface help visualize your repository?

## Challenge
Make a change directly on GitHub (edit a file through the web interface), then use `git pull` to sync it to your local repository.
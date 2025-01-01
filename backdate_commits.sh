#!/bin/bash

# Script to backdate commits in a Git repository
# Usage: ./backdate_commits.sh

set -e

echo "Git Commit Backdating Script"
echo "============================="
echo

# Function to backdate the last commit
backdate_last_commit() {
    echo "Current last commit:"
    git log -1 --format="%H %s (%ci)"
    echo
    
    read -p "Enter the date you want to backdate to (YYYY-MM-DD HH:MM:SS): " new_date
    
    if [[ ! "$new_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}$ ]]; then
        echo "Invalid date format. Please use YYYY-MM-DD HH:MM:SS"
        return 1
    fi
    
    # Amend the last commit with the new date
    GIT_COMMITTER_DATE="$new_date" git commit --amend --no-edit --date="$new_date"
    
    echo "Last commit backdated to: $new_date"
    echo "New commit info:"
    git log -1 --format="%H %s (%ci)"
}

# Function to backdate multiple commits interactively
backdate_multiple_commits() {
    echo "Recent commits:"
    git log --oneline -10
    echo
    
    read -p "Enter the number of commits to backdate (from most recent): " num_commits
    
    if ! [[ "$num_commits" =~ ^[0-9]+$ ]] || [ "$num_commits" -le 0 ]; then
        echo "Please enter a valid positive number"
        return 1
    fi
    
    echo "You will be prompted to enter a date for each of the last $num_commits commits"
    echo
    
    # Start interactive rebase
    git rebase -i HEAD~$num_commits --exec "
        echo 'Commit:' \$(git log -1 --format='%H %s')
        read -p 'Enter date for this commit (YYYY-MM-DD HH:MM:SS): ' commit_date
        if [[ \"\$commit_date\" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}$ ]]; then
            GIT_COMMITTER_DATE=\"\$commit_date\" git commit --amend --no-edit --date=\"\$commit_date\"
        else
            echo 'Invalid date format, skipping this commit'
        fi
    "
}

# Function to create commits with specific dates
create_backdated_commits() {
    echo "This will create new commits with backdated timestamps"
    echo
    
    while true; do
        read -p "Enter commit message (or 'done' to finish): " commit_msg
        
        if [ "$commit_msg" = "done" ]; then
            break
        fi
        
        read -p "Enter date for this commit (YYYY-MM-DD HH:MM:SS): " commit_date
        
        if [[ ! "$commit_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}$ ]]; then
            echo "Invalid date format. Please use YYYY-MM-DD HH:MM:SS"
            continue
        fi
        
        # Stage any changes
        git add .
        
        # Create commit with backdated timestamp
        GIT_COMMITTER_DATE="$commit_date" git commit --date="$commit_date" -m "$commit_msg"
        
        echo "Created backdated commit: $commit_msg"
    done
}

# Main menu
echo "Choose an option:"
echo "1. Backdate the last commit"
echo "2. Backdate multiple commits interactively"
echo "3. Create new backdated commits"
echo "4. Exit"
echo

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        backdate_last_commit
        ;;
    2)
        backdate_multiple_commits
        ;;
    3)
        create_backdated_commits
        ;;
    4)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo
echo "Remember to force push to update the remote repository:"
echo "git push --force-with-lease origin main"
echo
echo "WARNING: Force pushing rewrites history. Make sure your team is aware!"
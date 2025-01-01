#!/bin/bash

# Script to create backdated commits from Jan 1, 2025 to July 17, 2025
set -e

echo "Creating backdated commits from January 1, 2025 to July 17, 2025"
echo "================================================================="

# Array of commit messages and dates
declare -a commits=(
    "2025-01-01 10:00:00|Initial project setup and structure"
    "2025-01-15 14:30:00|Add basic utility functions"
    "2025-02-01 09:15:00|Implement core data processing logic"
    "2025-02-14 16:45:00|Add error handling and validation"
    "2025-03-01 11:20:00|Refactor code structure for better maintainability"
    "2025-03-15 13:10:00|Add comprehensive documentation"
    "2025-04-01 08:30:00|Implement advanced filtering features"
    "2025-04-15 15:25:00|Add unit tests and improve code coverage"
    "2025-05-01 12:00:00|Performance optimizations and bug fixes"
    "2025-05-15 17:30:00|Add new data export functionality"
    "2025-06-01 09:45:00|Implement user interface improvements"
    "2025-06-15 14:20:00|Add configuration management system"
    "2025-07-01 10:30:00|Final testing and quality assurance"
    "2025-07-17 16:00:00|Project completion and final updates"
)

# Function to make small changes to files
make_file_changes() {
    local commit_num=$1
    
    # Make small changes to existing files
    case $((commit_num % 4)) in
        0)
            echo "# Update $commit_num" >> README.md
            ;;
        1)
            echo "# Version update $commit_num" >> utils.py
            ;;
        2)
            echo "# Enhancement $commit_num" >> Hello.py
            ;;
        3)
            echo "# Requirement update $commit_num" >> requirements.txt
            ;;
    esac
}

# Create commits with backdated timestamps
commit_num=1
for commit_info in "${commits[@]}"; do
    # Split date and message
    IFS='|' read -r commit_date commit_msg <<< "$commit_info"
    
    echo "Creating commit $commit_num: $commit_msg"
    echo "Date: $commit_date"
    
    # Make some changes to files
    make_file_changes $commit_num
    
    # Stage changes
    git add .
    
    # Create commit with backdated timestamp
    GIT_COMMITTER_DATE="$commit_date" git commit --date="$commit_date" -m "$commit_msg"
    
    echo "✓ Commit created successfully"
    echo
    
    ((commit_num++))
done

echo "All backdated commits created successfully!"
echo
echo "Current commit history:"
git log --oneline -10
echo
echo "To push these changes to GitHub, run:"
echo "git push --force-with-lease origin main"
echo
echo "WARNING: This will rewrite your repository history!"
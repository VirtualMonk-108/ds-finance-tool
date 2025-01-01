#!/bin/bash

# Script to create daily commits from Jan 1 to July 17, 2025
set -e

echo "Creating daily commits from January 1 to July 17, 2025"
echo "====================================================="

# Arrays of commit messages for variety
declare -a commit_types=(
    "feat"
    "fix"
    "docs"
    "style"
    "refactor"
    "test"
    "chore"
    "perf"
    "ci"
    "build"
)

declare -a features=(
    "user authentication"
    "data processing pipeline"
    "export functionality"
    "configuration system"
    "error handling"
    "logging system"
    "API endpoints"
    "database integration"
    "caching layer"
    "validation rules"
    "notification system"
    "search functionality"
    "filtering options"
    "reporting module"
    "backup system"
    "security features"
    "performance monitoring"
    "batch processing"
    "real-time updates"
    "mobile support"
)

declare -a actions=(
    "implement"
    "update"
    "fix"
    "improve"
    "optimize"
    "refactor"
    "enhance"
    "add"
    "remove"
    "modify"
    "configure"
    "integrate"
    "test"
    "debug"
    "document"
)

# Function to generate random commit message
generate_commit_message() {
    local type=${commit_types[$((RANDOM % ${#commit_types[@]}))]}
    local feature=${features[$((RANDOM % ${#features[@]}))]}
    local action=${actions[$((RANDOM % ${#actions[@]}))]}
    
    echo "${type}: ${action} ${feature}"
}

# Function to make file changes
make_file_changes() {
    local day=$1
    local commit_num=$2
    local file_choice=$((RANDOM % 4))
    
    case $file_choice in
        0)
            echo "# Day $day, Commit $commit_num - $(date)" >> README.md
            ;;
        1)
            echo "# Update $day-$commit_num" >> utils.py
            ;;
        2)
            echo "# Enhancement $day-$commit_num" >> Hello.py
            ;;
        3)
            echo "# Version $day-$commit_num" >> requirements.txt
            ;;
    esac
}

# Function to get number of commits for a day (weighted to be more realistic)
get_commits_for_day() {
    local day_of_week=$1
    local random=$((RANDOM % 100))
    
    # Weekend days (Sat=6, Sun=0) - fewer commits
    if [[ $day_of_week == 0 || $day_of_week == 6 ]]; then
        if [[ $random -lt 30 ]]; then
            echo 0  # 30% chance of no commits
        elif [[ $random -lt 60 ]]; then
            echo 1  # 30% chance of 1 commit
        elif [[ $random -lt 85 ]]; then
            echo 2  # 25% chance of 2 commits
        else
            echo 3  # 15% chance of 3 commits
        fi
    # Weekdays - more commits
    else
        if [[ $random -lt 5 ]]; then
            echo 0  # 5% chance of no commits
        elif [[ $random -lt 25 ]]; then
            echo 1  # 20% chance of 1 commit
        elif [[ $random -lt 45 ]]; then
            echo 2  # 20% chance of 2 commits
        elif [[ $random -lt 65 ]]; then
            echo 3  # 20% chance of 3 commits
        elif [[ $random -lt 80 ]]; then
            echo 4  # 15% chance of 4 commits
        elif [[ $random -lt 90 ]]; then
            echo 5  # 10% chance of 5 commits
        elif [[ $random -lt 96 ]]; then
            echo 6  # 6% chance of 6 commits
        else
            echo 7  # 4% chance of 7 commits
        fi
    fi
}

# Function to generate random time
generate_random_time() {
    local hour=$((RANDOM % 14 + 8))  # 8 AM to 9 PM
    local minute=$((RANDOM % 60))
    local second=$((RANDOM % 60))
    printf "%02d:%02d:%02d" $hour $minute $second
}

# Generate commits for each day
current_date="2025-01-01"
end_date="2025-07-17"

total_commits=0

while [[ "$current_date" < "$end_date" ]] || [[ "$current_date" == "$end_date" ]]; do
    # Get day of week (0=Sunday, 6=Saturday)
    day_of_week=$(date -j -f "%Y-%m-%d" "$current_date" "+%w" 2>/dev/null || date -d "$current_date" "+%w")
    
    # Get number of commits for this day
    num_commits=$(get_commits_for_day $day_of_week)
    
    echo "Processing $current_date ($(date -j -f "%Y-%m-%d" "$current_date" "+%A" 2>/dev/null || date -d "$current_date" "+%A")): $num_commits commits"
    
    # Create commits for this day
    for ((i=1; i<=num_commits; i++)); do
        commit_msg=$(generate_commit_message)
        commit_time=$(generate_random_time)
        full_datetime="$current_date $commit_time"
        
        # Make changes to files
        make_file_changes "$current_date" "$i"
        
        # Stage changes
        git add .
        
        # Create commit
        GIT_COMMITTER_DATE="$full_datetime" git commit --date="$full_datetime" -m "$commit_msg" --quiet
        
        ((total_commits++))
    done
    
    # Move to next day
    if [[ "$OSTYPE" == "darwin"* ]]; then
        current_date=$(date -j -v+1d -f "%Y-%m-%d" "$current_date" "+%Y-%m-%d")
    else
        current_date=$(date -d "$current_date + 1 day" "+%Y-%m-%d")
    fi
done

echo
echo "✓ Successfully created $total_commits commits from January 1 to July 17, 2025"
echo
echo "Recent commit history:"
git log --oneline -15
echo
echo "To push these changes to GitHub, run:"
echo "git push --force-with-lease origin main"
echo
echo "WARNING: This will completely rewrite your repository history!"
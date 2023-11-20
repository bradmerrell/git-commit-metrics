import git
import os
import csv

def extract_commit_metrics(repository_url, local_repo_foldername):
    # Create the repo-metrics directory if it doesn't exist
    os.makedirs('./repo-metrics', exist_ok=True)

    # Set up paths
    repository_path = f"./repo-metrics/{local_repo_foldername}"
    csv_file_path = f"{repository_path}.csv"

    # Clone the repository if it's not already present
    if not os.path.exists(repository_path):
        git.Repo.clone_from(repository_url, repository_path)

    # Open the repository
    repo = git.Repo(repository_path)

    # Function to extract metrics from a commit
    def get_commit_metrics(commit):
        committer = commit.committer.name
        diffs = commit.diff(commit.parents[0] if commit.parents else git.NULL_TREE, create_patch=True)
        
        # Count added, deleted, and modified lines
        added_lines = sum(len(diff.diff.decode().split('\n')) for diff in diffs if diff.new_file)
        deleted_lines = sum(len(diff.diff.decode().split('\n')) for diff in diffs if diff.deleted_file)
        modified_lines = sum(len(diff.diff.decode().split('\n')) for diff in diffs if not diff.new_file and not diff.deleted_file)

        return committer, added_lines, modified_lines, deleted_lines

    # Extract metrics from each commit
    commit_metrics = [get_commit_metrics(commit) for commit in repo.iter_commits()]

    # Write to CSV
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Committer", "New Lines", "Updated Lines", "Deleted Lines"])
        writer.writerows(commit_metrics)

    return csv_file_path

# Prompt for user input
repository_url = input("Enter the repository URL: ")
local_repo_foldername = input("Enter the local repository folder name: ")

# Run the function
csv_path = extract_commit_metrics(repository_url, local_repo_foldername)
print(f"CSV file created at: {csv_path}")

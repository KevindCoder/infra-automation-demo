import subprocess

def run_playbook():
    result = subprocess.run(
        ['ansible-playbook', '-i', 'ansible/inventory.ini', 'ansible/playbook.yml'],
        capture_output=True,
        text=True
    )
    print("Output:\n", result.stdout)
    if result.stderr:
        print("Errors:\n", result.stderr)

if __name__ == "__main__":
    run_playbook()

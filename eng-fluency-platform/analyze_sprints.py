import glob
import re

files = sorted(glob.glob('sprints/sprint-*.md'))
total_unchecked = 0
total_checked = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Look for checklists: - [ ] and - [x]
        unchecked = len(re.findall(r'- \[\s\]', content))
        checked = len(re.findall(r'- \[x\]', content.lower()))
        
        if unchecked > 0 or checked > 0:
            print(f"{f}: {checked} implemented, {unchecked} pending")
        
        total_unchecked += unchecked
        total_checked += checked

print("="*40)
print(f"Total Implemented: {total_checked}")
print(f"Total Pending: {total_unchecked}")

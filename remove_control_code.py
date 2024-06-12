import os


def remove_prohibited_control_code(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()

        original_length = len(content)

        # U+0008 제어 코드, HTML 엔티티 및 UTF-8 인코딩 제거
        cleaned_content = content.replace("\x08", "")  # U+0008
        cleaned_content = cleaned_content.replace("&#8;", "")
        cleaned_content = cleaned_content.replace("&#x8;", "")
        cleaned_content = cleaned_content.replace("0x08", "")

        cleaned_length = len(cleaned_content)
        removed_count = original_length - cleaned_length

        if removed_count > 0:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(cleaned_content)

        return removed_count
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return 0


included_dirs = {"_posts", "_site", "_drafts"}
included_extensions = {".html", ".md"}

total_removed = 0
file_count = 0

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d in included_dirs]
    for file in files:
        if any(file.endswith(ext) for ext in included_extensions):
            file_path = os.path.join(root, file)
            if any(dir in file_path for dir in included_dirs):
                removed = remove_prohibited_control_code(file_path)
                if removed > 0:
                    print(
                        f"{removed} prohibited control code points removed from {file_path}"
                    )
                    total_removed += removed
                    file_count += 1

print(
    f"Total {total_removed} prohibited control code points removed from {file_count} files"
)

import os


def remove_prohibited_control_code(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()

    cleaned_content = content.replace("\x08", "")  # U+0008 제거

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(cleaned_content)

    print(f"Prohibited control code points removed from {file_path}")


# 포함할 디렉토리 목록
included_dirs = {"_posts", "_site"}

for root, dirs, files in os.walk("."):
    # 포함할 디렉토리만 탐색
    dirs[:] = [d for d in dirs if d in included_dirs]
    for file in files:
        file_path = os.path.join(root, file)
        if any(dir in file_path for dir in included_dirs):
            remove_prohibited_control_code(file_path)

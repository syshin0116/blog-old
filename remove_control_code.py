import os


def remove_prohibited_control_code(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()

    cleaned_content = content.replace("\x08", "")  # U+0008 제거

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(cleaned_content)

    print(f"Prohibited control code points removed from {file_path}")


# 전체 프로젝트 디렉토리에서 파일을 재귀적으로 검사하고 수정
for root, dirs, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        remove_prohibited_control_code(file_path)

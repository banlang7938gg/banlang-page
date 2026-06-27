#!/usr/bin/env python3
"""
ระบบคำนวณเกรด
โปรแกรมนี้คำนวณเกรดจากคะแนนตามเกณฑ์ดังนี้
- A: คะแนน >= 80
- B: คะแนน >= 70
- C: คะแนน >= 60
- D: คะแนน >= 50
- F: คะแนน < 50
"""


def get_grade(score):
    """
    รับข้อมูล (Input): คะแนน
    
    Args:
        score (float): คะแนน (0-100)
    
    Returns:
        str: เกรด (A, B, C, D, F)
    
    Raises:
        ValueError: ถ้าคะแนนไม่ใช่ตัวเลขหรือไม่อยู่ในช่วง 0-100
    """
    try:
        score = float(score)
    except (ValueError, TypeError):
        raise ValueError("❌ คะแนนต้องเป็นตัวเลข")
    
    if score < 0 or score > 100:
        raise ValueError("❌ คะแนนต้องอยู่ระหว่าง 0 ถึง 100")
    
    # โหลดข้อมูล (ตรวจเงื่อนไข)
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def display_result(score, grade):
    """
    แสดงผลลัพธ์
    
    Args:
        score (float): คะแนน
        grade (str): เกรด
    """
    grade_descriptions = {
        "A": "ดีเยี่ยม",
        "B": "ดี",
        "C": "พอใจ",
        "D": "ผ่าน",
        "F": "ไม่ผ่าน"
    }
    
    print("\n" + "=" * 40)
    print(f"คะแนน: {score}")
    print(f"เกรด: {grade} ({grade_descriptions[grade]})")
    print("=" * 40 + "\n")


def main():
    """โปรแกรมหลัก"""
    print("🎓 ระบบคำนวณเกรด")
    print("-" * 40)
    
    while True:
        try:
            # รับข้อมูล
            score_input = input("ใส่คะแนน (0-100) หรือพิมพ์ 'exit' เพื่อออก: ").strip()
            
            if score_input.lower() == 'exit':
                print("ขอบคุณที่ใช้งาน 👋\n")
                break
            
            if not score_input:
                print("❌ กรุณาใส่คะแนน\n")
                continue
            
            score = float(score_input)
            grade = get_grade(score)
            display_result(score, grade)
            
        except ValueError as e:
            print(f"❌ {e}\n")
        except KeyboardInterrupt:
            print("\n\nขอบคุณที่ใช้งาน 👋\n")
            break


if __name__ == "__main__":
    main()

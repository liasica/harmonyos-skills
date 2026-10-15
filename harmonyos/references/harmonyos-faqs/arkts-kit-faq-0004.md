---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0004
title: ArkTS-Record工具类型使用常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见问题 > ArkTS-Record工具类型使用常见问题
category: harmonyos-faqs
scraped_at: 2026-10-16T07:07:06+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:919adb25b949fbd4d2430f1d1ceadf49c267a4813824f1d9512ae6a99f2effc8
---

**Q：如何使用Record？**

**A**：构造一个对象类型，其属性键为“Keys” ，其属性值为“Type”，可用于将一种类型的属性映射到另一种类型。

示例如下：

```ts
// Define course types
type Course = 'Math' | 'Chinese' | 'English';

// Define grade types
type Grade = number;

// Define student grade record types
type StudentGrades = Record<Course, Grade>;

// Define the type of class grade record, where the key is the student ID and the value is the student's grade record
type ClassGrades = Record<string, StudentGrades>;

interface StudentCourseGrade {
  Math: number,
  Chinese: number,
  English: number
}

let student1: StudentCourseGrade = {
  Math: 90,
  Chinese: 85,
  English: 92
}
let student2: StudentCourseGrade = {
  Math: 78,
  Chinese: 82,
  English: 85
}
let student3: StudentCourseGrade = {
  Math: 95,
  Chinese: 89,
  English: 90
}

// Initialize class grades
const classGrades: ClassGrades = {
  '001': student1,
  '002': student2,
  '003': student3
};

@Entry
@Component
struct Index {
  // Obtain the average grade of a student
  getAverageGrade(studentId: string, grades: ClassGrades): number | null {
    const studentGrades = grades[studentId]; // Obtain corresponding grade data for students
    if (!studentGrades) {
      console.log(`Student with ID ${studentId} not found.`);
      return null;
    }

    const courses = Object.keys(studentGrades) as Course[]; // Course type array
    // Calculate the total grade of the course
    const total = courses.reduce((sum, course) => sum + studentGrades[course], 0);
    return total / courses.length; // Average score
  }

  build() {
    Row() {
      Column() {
        Button('getAverageGrade')
          .onClick(() => {
            // output: 89
            console.log('student average grade is:', this.getAverageGrade('001', classGrades));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

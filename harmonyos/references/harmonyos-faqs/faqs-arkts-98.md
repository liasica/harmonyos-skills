---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-98
title: 如何使用Record
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何使用Record
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:77d1beb54310e4b947ef5fe1d186ca65eb02687be1e17e8f5caae025d85a5646
---

构造一个对象类型，其属性键为“Keys” ，其属性值为“Type”，可用于将一种类型的属性映射到另一种类型。

示例如下：

```
1. // Define course types
2. type Course = 'Math' | 'Chinese' | 'English';

5. // Define grade types
6. type Grade = number;

9. // Define student grade record types
10. type StudentGrades = Record<Course, Grade>;

13. // Define the type of class grade record, where the key is the student ID and the value is the student's grade record
14. type ClassGrades = Record<string, StudentGrades>;

17. interface StudentCourseGrade {
18. Math: number,
19. Chinese: number,
20. English: number
21. }

24. let student1: StudentCourseGrade = {
25. Math: 90,
26. Chinese: 85,
27. English: 92
28. }
29. let student2: StudentCourseGrade = {
30. Math: 78,
31. Chinese: 82,
32. English: 85
33. }
34. let student3: StudentCourseGrade = {
35. Math: 95,
36. Chinese: 89,
37. English: 90
38. }

41. // Initialize class grades
42. const classGrades: ClassGrades = {
43. '001': student1,
44. '002': student2,
45. '003': student3
46. };

49. @Entry
50. @Component
51. struct Index {
52. // Obtain the average grade of a student
53. getAverageGrade(studentId: string, grades: ClassGrades): number | null {
54. const studentGrades = grades[studentId]; // Obtain corresponding grade data for students
55. if (!studentGrades) {
56. console.log(`Student with ID ${studentId} not found.`);
57. return null;
58. }

61. const courses = Object.keys(studentGrades) as Course[]; // Course type array
62. // Calculate the total grade of the course
63. const total = courses.reduce((sum, course) => sum + studentGrades[course], 0);
64. return total / courses.length; // Average score
65. }

68. build() {
69. Row() {
70. Column() {
71. Button('getAverageGrade')
72. .onClick(() => {
73. // output: 89
74. console.log('student average grade is:', this.getAverageGrade('001', classGrades));
75. })
76. }
77. .width('100%')
78. }
79. .height('100%')
80. }
81. }
```

[UseRecord.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/UseRecord.ets#L21-L101)

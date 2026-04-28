---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-avoid-overusing-custom-component-check
title: @performance/avoid-overusing-custom-component-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/avoid-overusing-custom-component-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:58+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8191c9381a278ebd9b497c79939515d8583e4f2124aa363c7929649bba193315
---

当在应用中使用自定义组件时，可以优先使用@Builder函数代替自定义组件，@Builder函数不会在后端FrameNode节点树上创建一个新的树节点，有助于缩短页面的加载和渲染时长。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/avoid-overusing-custom-component-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 1. 自定义@Builder函数组件
2. @Builder
3. function UserCardBuilder(name: string, age?: number, avatarImage?: ResourceStr) {
4. Row() {
5. Row() {
6. Image(avatarImage)
7. .size({ width: 50, height: 50 })
8. .borderRadius(25)
9. .margin(8)
10. Text(name)
11. .fontSize(30)
12. }

14. Text(`年龄：${age?.toString()}`)
15. .fontSize(20)
16. }
17. .backgroundColor(DEFAULT_BACKGROUND_COLOR)
18. .justifyContent(FlexAlign.SpaceBetween)
19. .borderRadius(8)
20. .padding(8)
21. .height(66)
22. .width('80%')
23. }

25. @Component
26. export struct UserCardList {
27. @State users: User[] = getUsers();

29. aboutToAppear(): void {
30. let message = 'hello world';
31. }

33. build() {
34. List({ space: 8 }) {
35. ForEach(this.users, (item: User) => {
36. ListItem() {
37. // 2. 使用@Builder函数
38. UserCardBuilder(item.name, item.age, item.avatarImage)
39. }
40. }, (item: User) => item.id)
41. }
42. .alignListItem(ListItemAlign.Center)
43. }
44. }
```

## 反例

```
1. import { util } from '@kit.ArkTS';

3. interface User {
4. id: string;
5. name: string;
6. age?: number;
7. avatarImage?: ResourceStr;
8. // introduction: string;
9. // ...
10. }

12. // 构造数据
13. const DEFAULT_BACKGROUND_COLOR = Color.Pink;
14. const getUsers = () => {
15. const USERS: User[] = [{
16. id: '1',
17. name: '张三',
18. }, {
19. id: '2',
20. name: '李四',
21. }, {
22. id: '3',
23. name: '王五',
24. }];
25. return Array.from(Array(30), (item: User, i: number) => {
26. return {
27. id: util.generateRandomUUID(),
28. name: USERS[i%3].name,
29. avatarImage: $r('app.media.avatar'),
30. age: 18 + i
31. } as User;
32. });
33. }

35. // 用户卡片列表组件
36. @Component
37. export struct UserCardList {
38. @State users: User[] = getUsers();

40. build() {
41. List({ space: 8 }) {
42. ForEach(this.users, (item: User) => {
43. ListItem() {
44. UserCard({ name: item.name, age: item.age, avatarImage: item.avatarImage })
45. }
46. }, (item: User) => item.id)
47. }
48. .alignListItem(ListItemAlign.Center)
49. }
50. }

52. // 用户卡片自定义组件
53. @Component
54. struct UserCard {
55. @Prop avatarImage: ResourceStr;
56. @Prop name: string;
57. @Prop age: number;

59. build() {
60. Row() {
61. Row() {
62. Image(this.avatarImage)
63. .size({ width: 50, height: 50 })
64. .borderRadius(25)
65. .margin(8)
66. Text(this.name)
67. .fontSize(30)
68. }

70. Text(`年龄：${this.age.toString()}`)
71. .fontSize(20)
72. }
73. .backgroundColor(DEFAULT_BACKGROUND_COLOR)
74. .justifyContent(FlexAlign.SpaceBetween)
75. .borderRadius(8)
76. .padding(8)
77. .height(66)
78. .width('80%')
79. }
80. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。

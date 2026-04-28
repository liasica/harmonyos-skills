---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-ffrt-no-use-std
title: @performance/hp-ffrt-no-use-std
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-ffrt-no-use-std
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d1d349222e6799ba36be404cd7f03b084c51e5681b4a693801a2f4f231c67587
---

禁止在FFRT worker中使用std::xxx等同步接口。该规则仅对C/C++文件进行检查。

并行化场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-ffrt-no-use-std": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. #include <iostream>
2. #include <algorithm>
3. #include <mutex>
4. #include <condition_variable>
5. #include <unistd.h>
6. // ffrt头文件
7. #include "ffrt/ffrt.h"
8. using namespace std;
9. int N = 100;
10. int M = 100;

12. // ffrt::submit中使用了std::mutex
13. void PositiveCase1(int temp) {
14. ffrt::mutex lock;
15. int acc = 0;
16. for (int i = 0; i < N; ++i) {
17. ffrt::submit(
18. [&]() {
19. for (int j = 0; j < M; ++j) {
20. lock.lock();
21. acc++;
22. lock.unlock();
23. }
24. },
25. {}, {});
26. }
27. }
28. // ffrt::submit中使用了std::condition_variable
29. void PositiveCase2(int temp) {
30. ffrt::condition_variable cond;
31. int a = 0;
32. ffrt::mutex lock_;
33. ffrt::submit(
34. [&]() {
35. std::unique_lock<ffrt::mutex> lck(lock_);
36. cond.wait(lck, [&] { return a == 1; });
37. },
38. {}, {});
39. ffrt::submit(
40. [&]() {
41. std::unique_lock<ffrt::mutex> lck(lock_);
42. a = 1;
43. cond.notify_one();
44. },
45. {}, {});
46. ffrt::wait();
47. }
48. // ffrt::submit中使用了std::usleep
49. void PositiveCase3(int temp) {
50. ffrt::submit(
51. [&]() {
52. ffrt_usleep(100);
53. printf("test");
54. ffrt_yield();
55. }, {}, {});
56. }
57. // ffrt::submit中使用了pthread_rwlock_wrlock或pthread_rwlock_rdlock
58. void PositiveCase4(int temp) {
59. int a = 0;
60. ffrt_rwlock_t mtx;
61. ffrt::submit(
62. [&]() {
63. int ret = ffrt_rwlock_wrlock(&mtx);
64. if (ret != ffrt_success) {
65. printf("error\n");
66. }
67. a++;
68. ret = ffrt_rwlock_unlock(&mtx);
69. if (ret != ffrt_success) {
70. printf("error\n");
71. }
72. }, {}, {});
73. ffrt::submit(
74. [&]() {
75. int ret = ffrt_rwlock_rdlock(&mtx);
76. if (ret != ffrt_success) {
77. printf("error\n");
78. }
79. printf("sum is %d\n", a);
80. ret = ffrt_rwlock_unlock(&mtx);
81. if (ret != ffrt_success) {
82. printf("error\n");
83. }
84. }, {}, {});
85. }
```

## 反例

```
1. #include <iostream>
2. #include <algorithm>
3. #include <mutex>
4. #include <condition_variable>
5. #include <unistd.h>
6. // ffrt头文件
7. #include "ffrt/ffrt.h"
8. using namespace std;
9. int N = 100;
10. int M = 100;
11. // ffrt::submit中使用了std::mutex
12. void NegativeCase1(int temp) {
13. std::mutex lock;
14. int acc = 0;
15. for (int i = 0; i < N; ++i) {
16. ffrt::submit(
17. [&]() {
18. for (int j = 0; j < M; ++j) {
19. lock.lock();
20. acc++;
21. lock.unlock();
22. }
23. },
24. {}, {});
25. }
26. }
27. // ffrt::submit中使用了std::condition_variable
28. void NegativeCase2(int temp) {
29. std::condition_variable cond;
30. int a = 0;
31. std::mutex lock_;
32. ffrt::submit(
33. [&]() {
34. std::unique_lock<std::mutex> lck(lock_);
35. cond.wait(lck, [&] { return a == 1; });
36. },
37. {}, {});
38. ffrt::submit(
39. [&]() {
40. std::unique_lock<std::mutex> lck(lock_);
41. a = 1;
42. cond.notify_one();
43. },
44. {}, {});
45. ffrt::wait();
46. }
47. // ffrt::submit中使用了std::usleep
48. void NegativeCase3(int temp) {
49. ffrt::submit(
50. [&]() {
51. usleep(100);
52. printf("test");
53. ffrt_yield();
54. }, {}, {});
55. }
56. // ffrt::submit中使用了pthread_rwlock_wrlock或pthread_rwlock_rdlock
57. void NegativeCase4(int temp) {
58. int a = 0;
59. pthread_rwlock_t mtx;
60. ffrt::submit(
61. [&]() {
62. int ret = pthread_rwlock_wrlock(&mtx);
63. if (ret != 0) {
64. printf("error\n");
65. }
66. a++;
67. ret = pthread_rwlock_unlock(&mtx);
68. if (ret != 0) {
69. printf("error\n");
70. }
71. }, {}, {});
72. ffrt::submit(
73. [&]() {
74. int ret = pthread_rwlock_rdlock(&mtx);
75. if (ret != 0) {
76. printf("error\n");
77. }
78. printf("sum is %d\n", a);
79. ret = pthread_rwlock_unlock(&mtx);
80. if (ret != 0) {
81. printf("error\n");
82. }
83. }, {}, {});
84. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。

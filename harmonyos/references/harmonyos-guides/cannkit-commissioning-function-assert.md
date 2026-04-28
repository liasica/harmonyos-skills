---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-function-assert
title: assert功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > 更多功能 > assert功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d615cf201450538aa1710b56e257ad110e4d0cb6e0c4e9be9e378031e0227696
---

## 功能介绍

使用工具进行算子调测时，支持断言功能。当核函数代码中条件判断为false时，则立即中断运行流程并打印相关信息，方便快速定位错误。

说明

固定为每个核分配的打印数据的最大可使用空间为1M，目前该大小不支持修改，若打印超过1M，打印内容不再显示，请开发者控制待打印的数据量。

## 使用方法（命令行）

1. 在核函数代码中根据需要，在目标位置调用assert接口，详情请参见接口说明，样例如下。

   ```
   1. int32_t x = 31;
   2. assert(x < 0, "Invalid input_num: %d\n", x);
   ```
2. simulator调测场景执行如下命令，使能Dump开关。

   ```
   1. ascendebug kernel --backend simulator --dump-mode normal ... {其他simulator调测参数}
   ```

   --dump-mode取normal，开启通用打印Scalar模式，其他参数参考[NPU调测参数](cannkit-cli-parameters.md#npu调测参数)根据需要进行配置。
3. 查看断言结果。

   若调用时传入的判断条件为false，会中断程序并在屏幕上显示断言内容（带文件名、行号），结果示例如下。

   ```
   1. [ASSERT] /home/.../add_custom.cpp:94: Assertion `x < 0' Invalid input_num: 31
   ```

## 接口说明

assert接口说明如下。

* **函数原型：** \_\_aicore\_\_ inline void assert(bool assertFlag, \_\_gm\_\_ const char\* fmt, Args&&... args);
* **函数功能：** 用于程序调试。在程序运行时检查一个条件是否为真，若条件为假，立即中断程序并打印信息。
* **参数(IN)：**

  + **assertFlag：** 判断是否要中断程序打印断言语句的条件。
    - false：程序中断退出，在屏幕上显示assert传入的打印内容。
    - true： 程序不会在assert中断，无打印。
  + **fmt：** 开发者输入常量字符串，作为打印的前缀修饰。
  + **args：** 开发者需要打印的变量名。
* **参数(OUT)：** NA
* **返回值：** NA
* **使用约束：**

  + 不支持转义字符打印。
  + 当前支持的上板打印类型同[printf/PRINTF功能](cannkit-commissioning-function-printf.md)。
* **调用示例：**

  ```
  1. assert(input_num > 0, "Invalid input_num: %d ", input_num);
  ```

  + 若input\_num==0，程序中断，打印内容为“[ASSERT] /path\_to/add\_custom\_test.cpp:25 Invalid input\_num: 0”。
  + 若input\_num>0，程序不会在assert处中断。

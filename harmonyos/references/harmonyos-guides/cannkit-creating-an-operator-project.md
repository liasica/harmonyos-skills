---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-creating-an-operator-project
title: 创建算子工程
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 工程化算子开发 > 创建算子工程
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ff1aa7d839e49418e871cea0a46865dbd0ffe3a22f0bf842152f80571f266c29
---

DDK开发套件包中提供了自定义算子工程生成工具msOpGen，可基于算子原型定义输出算子工程：包括**算子host侧代码实现文件**、**算子kernel侧实现文件**以及**工程编译配置文件等**。

**简要说明：**

使用msOpGen工具创建算子工程之前，需要参考[环境准备](cannkit-environment-preparation.md)章节安装驱动固件和DDK软件包，完成开发环境和运行环境的准备。

同时需要配置ascendc环境变量，示例如下。

```
1. source ddk/tools/tools_ascendc/set_ascendc_env.sh
```

使用msOpGen工具创建算子开发工程的步骤如下。

1. 编写算子的原型定义json文件，用于生成算子开发工程。

   例如，AddCustom算子的json文件命名为add\_custom.json，文件内容如下。

   ```
   1. [
   2. {
   3. "op": "AddCustom",
   4. "input_desc": [
   5. {
   6. "name": "x",
   7. "param_type": "required",
   8. "format": [
   9. "ND",
   10. "ND",
   11. "ND"
   12. ],
   13. "type": [
   14. "fp16",
   15. "float",
   16. "int32"
   17. ]
   18. },
   19. {
   20. "name": "y",
   21. "param_type": "required",
   22. "format": [
   23. "ND",
   24. "ND",
   25. "ND"
   26. ],
   27. "type": [
   28. "fp16",
   29. "float",
   30. "int32"
   31. ]
   32. }
   33. ],
   34. "output_desc": [
   35. {
   36. "name": "z",
   37. "param_type": "required",
   38. "format": [
   39. "ND",
   40. "ND",
   41. "ND"
   42. ],
   43. "type": [
   44. "fp16",
   45. "float",
   46. "int32"
   47. ]
   48. }
   49. ]
   50. }
   51. ]
   ```

   例如，ReduceMaxCustom算子（包含属性）的json文件命名为reduce\_max\_custom.json，文件内容如下。

   ```
   1. [
   2. {
   3. "op": "ReduceMaxCustom",
   4. "input_desc": [
   5. {
   6. "name": "x",
   7. "param_type": "required",
   8. "format": ["ND"],
   9. "type": ["float16"]
   10. }
   11. ],
   12. "output_desc": [
   13. {
   14. "name": "y",
   15. "param_type": "required",
   16. "format": ["ND"],
   17. "type": ["float16"]
   18. },
   19. {
   20. "name": "idx",
   21. "param_type": "required",
   22. "format": ["ND"],
   23. "type": ["int32"]
   24. }
   25. ],
   26. "attr": [
   27. {
   28. "name": "reduceDim",
   29. "param_type": "required",
   30. "type": "int"
   31. },
   32. {
   33. "name": "isKeepDim",
   34. "param_type": "optional",
   35. "type": "int",
   36. "default_value": 1
   37. }
   38. ]
   39. }
   40. ]
   ```
2. 使用msOpGen工具生成算子的开发工程。以生成AddCustom的算子工程为例，下文仅针对关键参数进行解释，详细参数说明请参见[算子工程创建工具参数说明](cannkit-creating-operator-project-msopgen.md)。

   ```
   1. msopgen gen -i ./add_custom.json -c ai_core-kirin9020 -f ONNX -out ./AddCustom
   ```

   * -i：指定算子原型定义文件add\_custom.json所在路径，请根据实际情况修改。
   * -c：ai\_core-<soc\_version>代表算子在AI Core上执行，<soc\_version>为AI处理器的型号，当前支持ai\_core-kirin9020。

   说明

   AI处理器的型号<soc\_version>请在运行环境上通过命令行获取：

   hdc -t {target} shell param get ohos.boot.chiptype

   target：设备的SN码，可以通过hdc list targets获取当前环境上所有设备的SN码。

   * -f：第三方算子平台，目前支持TF、ONNX。
   * -out：生成文件所在路径，可配置为绝对路径或者相对路径，并且工具执行开发者对路径具有可读写权限。若不配置，则默认生成在执行命令的当前路径。
3. 命令执行完后，会在-out指定目录或者默认路径下生成算子工程目录，工程中包含算子实现的模板文件，编译脚本等，以AddCustom算子为例，目录结构如下所示：

   ```
   1. AddCustom
   2. ├── build_devices.sh    // 编译kernel动态库入口脚本
   3. ├── build.sh            // 编译入口脚本
   4. ├── cmake
   5. │   ├── config.cmake
   6. │   ├── func.cmake
   7. │   ├── intf.cmake
   8. │   ├── makeself.cmake
   9. │   └── util           // 算子工程编译所需脚本及公共编译文件存放目录
   10. ├── CMakeLists.txt     // 算子工程的CMakeLists.txt
   11. ├── CMakePresets.json  // 编译配置项
   12. ├── framework          // 算子插件实现文件目录，单算子模型文件的生成不依赖算子适配插件，无需关注
   13. ├── op_host                    // host侧实现文件
   14. │   ├── add_custom_tiling.h    // 算子tiling定义文件
   15. │   ├── add_custom.cpp         // 算子原型注册、shape推导、信息库、tiling实现等内容文件
   16. │   ├── CMakeLists.txt
   17. ├── op_kernel                  // kernel侧实现文件
   18. │   ├── CMakeLists.txt
   19. │   ├── add_custom.cpp         // 算子代码实现文件
   20. └── scripts                    // 自定义算子工程打包相关脚本所在目录
   ```

   说明

   上述目录结构中的粗体文件为后续算子开发过程中需要修改的文件，其他文件无需修改。

工程目录中的op\_kernel和op\_host包含了算子的核心实现文件。op\_kernel下存放[Kernel侧算子实现](cannkit-operator-implementation-on-the.md)。op\_host下存放host侧代码实现，包括[算子原型定义实现](cannkit-operator-prototype-definition.md)、[Host侧Tiling实现](cannkit-tiling-implementation-on-the-host.md)。其中kernel侧算子实现和host侧tiling实现在[算子实现](cannkit-operator-implementation-overview.md)章节已经介绍了其核心的实现方法，在该章节会侧重于介绍接入DDK框架后的编程模式和API的使用。工程目录中的CMakePresets.json，用于开发者完成工程编译相关配置，之后即可进行编译部署。

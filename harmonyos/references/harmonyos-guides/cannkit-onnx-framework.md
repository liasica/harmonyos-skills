---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-onnx-framework
title: ONNX框架
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子部署 > AI框架算子适配 > ONNX框架
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:17519c30aed7969ac998cbe9e6ca711dabf12685335f494696ce9e55e995b84d
---

## 适配插件开发

开发者可以参考本章节进行算子适配插件的开发，将ONNX框架的算子映射成适配Kirin AI处理器的算子（下文简称AscendC算子），从而完成从ONNX框架调用AscendC自定义算子的过程。如下样例展示了一个基础的开发流程：

```
1. #include "register/register.h"
2. #include "nlohmann/json.hpp"
3. namespace domi {
4. Status ParseParamByOpFunc(const ge::Operator& op_src, ge::Operator& op_dest) {
5. // ...
6. }
7. REGISTER_CUSTOM_OP("OpType")    // 映射的自定义算子类型
8. .FrameworkType(ONNX)
9. .OriginOpType("OriginOpType")  // ONNX模型中的算子类型
10. .ParseParamsByOperatorFn(ParseParamByOpFunc);   // 用来注册解析算子属性的函数
11. }
```

1. 包含所需头文件。

   * register.h，存储在DDK软件安装后文件存储路径的"ddk/ai\_ddk\_lib/include/register"目录下，包含该头文件，可使用算子注册相关类，调用算子注册相关的接口。
   * json.hpp，用于进行ONNX数据定义的解析，将String类型的算子参数定义转换为json格式。若样例工程中未提供"json.hpp"文件，开发者可以自行下载，并将"json.hpp"放在工程可以找到的任意路径下，然后包含此头文件即可，推荐放在DDK安装目录的"tools/tools\_ascendc/json-develop"下，按如下目录放置。下载路径可参见[json.hpp](https://github.com/nlohmann/json/blob/develop/single_include/nlohmann/json.hpp)。

     ```
     1. json-develop
     2. ├── include
     3. │   └── nlohmann
     4. │       └── json.hpp
     5. └── README.md
     ```
2. 使用REGISTER\_CUSTOM\_OP宏，完成DDK算子和ONNX框架的算子映射关系注册。使用方法如下。

   * REGISTER\_CUSTOM\_OP：注册自定义算子，OpType为算子类型名称，需要与[算子原型定义实现](cannkit-operator-prototype-definition.md)中的OpType保持一致。
   * [FrameworkType](cannkit-frameworktype.md)：ONNX代表原始框架为ONNX。
   * [OriginOpType](cannkit-originoptype.md)：算子在原始框架中的类型。例如自定义算子OpTypeA，对应ONNX算子库版本opset\_version=11，应传入"ai.onnx::11::OpTypeA"，当前支持的ONNX版本范围为9~15。
   * [ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)(ParseParamByOpFunc)：用来注册解析算子参数实现映射关系的回调函数，需要开发者自定义实现[ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)。具体实现方式参考步骤3。
3. 实现回调函数ParseParamByOpFunc。其函数声明如下所示：

   ```
   1. Status ParseParamByOpFunc(const ge::Operator& op_src, ge::Operator& op_dest)
   ```

   * ParseParamByOpFunc：函数名称，开发者自定义。
   * op\_src：ONNX框架定义的Operator类对象，包含ONNX模型中自定义的算子属性信息，定义来源于ONNX框架的原始模型文件。
   * op\_dest：DDK算子数据结构，保存算子信息，Operator类的详细描述请参见[Operator](cannkit-operator-construction-and-destructor.md)。

   开发者需要在回调函数中实现属性的解析和映射，具体实现方式如下。

   ONNX原始模型中，属性为repeated message类型，对于repeated message类型的参数，可使用**GetAttr(const char \*name, ge::AscendString &attr\_value)** 接口获取其属性值，然后将AscendString类型的属性值转换为String类型，再将其转换为json格式进行属性字段的解析。

   实现如下所示：

   ```
   1. SStatus ParseParamAddCustom(const ge::Operator& op_src, ge::Operator& op_dest) {
   2. ge::AscendString attrs_string;
   3. // 使用固定属性名称“attribute”获取ONNX算子中的属性，并赋值给AscendString类型对象
   4. if (ge::GRAPH_SUCCESS == op_src.GetAttr("attribute", attrs_string)) {
   5. nlohmann::json attrs = nlohmann::json::parse(attrs_string.GetString());
   6. for (nlohmann::json attr : attrs["attribute"]) {
   7. if (attr["name"] == "bias") {
   8. int64_t bias  = attr["i"];
   9. op_dest.SetAttr("bias", bias);
   10. }
   11. }
   12. }
   13. return SUCCESS;
   14. }
   ```

   开发者也可以使用自动解析和映射的回调函数AutoMappingByOpFn，使用方式如下。

   ```
   1. #include "register/register.h"
   2. namespace domi {
   3. REGISTER_CUSTOM_OP("OpType")
   4. .FrameworkType(ONNX)
   5. .OriginOpType("OriginOpType")
   6. .ParseParamsByOperatorFn(AutoMappingByOpFn);   // 用来注册解析算子属性的函数
   7. }
   ```

   说明

   * 当前版本GetAttr与SetAttr接口不支持对原始文件中数据类型为double和uint64的字段进行解析。
   * 使用omg工具执行模型转换时，对属性的获取情况不会进行强校验。所以进行算子适配插件实现时，若开发者调用GetAttr失败，建议根据算子实际情况增加相应的处理逻辑，例如，针对必选属性，可返回失败，针对可选属性，可设置默认值。
   * 对于float32的非常量输入，如果算子注册只支持float16, 框架会自动插入cast算子将float32的输入转成float16的输入，计算完成后通过cast算子将输出转回float32的输出。对于float32的常量输入，框架不会自动转换，需要开发者自行修改权重格式、类型，以匹配算子的输入。

## 调用样例

完成了ONNX框架的适配插件开发后，即可实现从ONNX框架调用AscendC自定义算子。下面以一个仅包含AddCustom算子的ONNX框架网络为例（该网络中的AddCustom算子通过适配插件映射为自定义的AddCustom算子），呈现一个使用推理工具进行推理的过程，目的在于让开发者快速体验推理场景下网络中自定义算子调用的过程。

在完成如下步骤之前，开发者需要先参考上文内容完成自定义AddCustom算子kernel侧和host侧的开发、ONNX适配插件的开发，并完成算子的编译部署。

完整样例请参考[AddCustom算子实现](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp)和[ONNX框架调用示例](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/Onnx/create_addcustom_onnx.py) 。

1. 通过pytorch代码生成该自定义算子。

   ```
   1. import os
   2. import numpy as np
   3. import onnx
   4. from onnx import helper
   5. from onnx import TensorProto

   8. def create_model():
   9. AddCustom = helper.make_node(
   10. "AddCustom",
   11. inputs = ["input1", "input2"],
   12. outputs = ["output"],
   13. name = "add",
   14. bias = 1
   15. )

   17. input1_input = helper.make_tensor_value_info("input1", TensorProto.FLOAT, [8, 2048])
   18. input2_input = helper.make_tensor_value_info("input2", TensorProto.FLOAT, [8, 2048])
   19. add_output = helper.make_tensor_value_info('output', TensorProto.FLOAT, [8, 2048])

   21. graph = helper.make_graph(
   22. nodes = [AddCustom],
   23. name = 'custom_graph',
   24. inputs = [input1_input, input2_input],
   25. outputs = [add_output]
   26. )

   28. model = helper.make_model(graph, producer_name='onnx-example')
   29. model.opset_import[0].version = 11
   30. model.ir_version = 6

   32. return model

   34. model = create_model()
   35. print(onnx.helper.printable_graph(model.graph))
   36. onnx.save(model, "./add_custom.onnx")
   ```
2. 在%{DDK\_INSTALL\_PATH}/tools/tools\_omg执行如下命令生成离线模型。（如下命令中使用的目录以及文件均为样例，请以实际为准）

   ```
   1. ./omg --model ./add_custom.onnx --framework 5 --output out/custom_graph --target=omc
   ```

   关键参数的解释如下。

   * --model：ONNX框架网络模型文件（\*.onnx）的路径。
   * --framework：原始框架类型。5表示ONNX。
   * --output：转换后的离线模型的路径以及文件名。请注意，记录保存该omc模型文件的路径，后续开发应用时需要使用。
   * --target：转换后的模型类型，自定义算子场景仅支持omc。
   * --platform：omc模型为硬件相关模型，指定omc模型运行的芯片平台。

     说明

     模型转换命令相关参数参考[离线模型转换](../hiai-Guides/offline-model-conversion-0000001053807006.md)。
3. 若提示有出现如下信息，则说明进入了AscendC自定义算子编译流程且模型转换成功。

   ```
   1. // ...
   2. "the node AddCustom is custom node"
   3. // ...
   4. "OMG generate offline model success."
   ```

   成功执行命令后，在--output参数指定的路径下，可查看离线模型（如：leaky\_relu.om）。
4. 参考[生成输入数据](cannkit-graph-compilation-and-execution.md#生成输入数据)准备符合模型输入要求的\*.bin格式的输入数据。
5. 参考[APP集成代码](cannkit-graph-compilation-and-execution.md#app集成代码)，完成模型集成。

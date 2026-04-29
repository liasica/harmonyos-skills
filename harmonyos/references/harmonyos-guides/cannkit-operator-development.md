---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-development
title: 快速入门
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 快速入门
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a235daac0f2c2788060d983c32f8ff961305501caea2f4c987b812c86bbc758d
---

本节以一个简单算子为例，带开发者体验从算子工程创建、代码编写、编译部署到运行验证的开发全流程，让开发者对算子开发工程有个宏观的认识，此处我们以输入是动态shape的Add算子实现为例，为了与内置Add算子区分，定义算子类型为AddCustom。

## 工程创建

DDK软件包中提供了工程创建工具msOpGen，开发者可以输入算子原型定义文件生成AscendC算子开发工程。

1. 编写AddCustom算子的原型定义json文件。

   假设AddCustom算子的原型定义文件命名为add\_custom.json，存储路径为: $HOME/sample，文件内容如下。

   ```
   1. [
   2. {
   3. "op": "AddCustom",
   4. "input_desc": [
   5. {
   6. "name": "x",
   7. "param_type": "required",
   8. "format": [
   9. "ND"
   10. ],
   11. "type": [
   12. "fp16"
   13. ]
   14. },
   15. {
   16. "name": "y",
   17. "param_type": "required",
   18. "format": [
   19. "ND"
   20. ],
   21. "type": [
   22. "fp16"
   23. ]
   24. }
   25. ],
   26. "output_desc": [
   27. {
   28. "name": "z",
   29. "param_type": "required",
   30. "format": [
   31. "ND"
   32. ],
   33. "type": [
   34. "fp16"
   35. ]
   36. }
   37. ]
   38. }
   39. ]
   ```
2. 注意先设置环境变量，执行**source ${install\_path}/ddk/** **tools/tools\_ascendc/set\_ascendc\_env.sh**命令，其中${install\_path}为tools包的解压目录。
3. 使用msOpGen工具生成AddCustom算子的开发工程。

   ```
   1. msopgen gen -i $HOME/sample/add_custom.json -c ai_core-<soc_version> -out   $HOME/sample/AddCustom
   ```

   * -i：算子原型定义文件add\_custom.json所在路径。
   * -c：ai\_core-<soc\_version>代表算子在AI Core上执行，<soc\_version>为Kirin AI处理器的型号，可在运行环境通过命令进行查询:

     ```
     1. hdc -t ${target} shell param get ohos.boot.chiptype
     ```

     target：设备的SN码，可以通过hdc list targets获取当前运行环境上所有设备的SN码。

   样例：

   ```
   1. msopgen gen -i ./add_custom.json -c ai_core-kirin9020 -out ./AddCustom
   ```

   基于同系列的AI处理器型号创建的算子工程，其基础能力通用。命令执行完后，会在$HOME/sample目录下生成算子工程目录AddCustom，工程中包含算子实现的模板文件，编译脚本等，如下所示。

   ```
   1. AddCustom
   2. ├── build_devices.sh // 开发者无需关注，在线编译场景预留，编译device侧交付件脚本
   3. ├── build.sh         // 编译入口脚本
   4. ├── cmake
   5. │   ├── config.cmake
   6. │   ├── util        // 算子工程编译所需脚本及公共编译文件存放目录
   7. ├── CMakeLists.txt   // 算子工程的CMakeLists.txt
   8. ├── CMakePresets.json // 编译配置项
   9. ├── framework        // 算子插件实现文件目录，单算子模型文件的生成不依赖算子适配插件，无需关注
   10. ├── op_host                      // host侧实现文件
   11. │   ├── add_custom_tiling.h    // 算子tiling定义文件
   12. │   ├── add_custom.cpp         // 算子原型注册、shape推导、信息库、tiling实现等内容文件
   13. │   ├── CMakeLists.txt
   14. ├── op_kernel                   // kernel侧实现文件
   15. │   ├── CMakeLists.txt
   16. │   ├── add_custom.cpp        // 算子核函数实现文件
   17. ├── scripts                     // 自定义算子工程打包相关脚本所在目录
   ```

   说明

   上述目录结构中的粗体文件op\_host/add\_custom\_tiling.h、op\_host/add\_custom.cpp、op\_kernel/add\_custom.cpp为后续算子开发过程中需要修改的文件，其他文件无需修改。

## 算子核函数实现

在工程存储目录的"AddCustom/op\_kernel/add\_custom.cpp"文件中实现算子的核函数，完整的样例代码开发者可以在[add\_custom.cpp](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/AddCustom/op_kernel/add_custom.cpp)中查看，下面介绍关键实现代码。

算子核函数实现代码的内部调用关系示意图如下。

**图1** 核函数调用关系图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/F75iGJHRRNS_eod3wOI-8g/zh-cn_image_0000002589245535.png?HW-CC-KV=V1&HW-CC-Date=20260429T054100Z&HW-CC-Expire=86400&HW-CC-Sign=1C39BB3376D59B83CB69D645E1CA9AC6574AE8830FBFA3F6781D6A10AAB6FB84)

由此可见除了Init函数完成初始化外，Process中完成了对流水任务 **：** 搬入、计算、搬出的调用，开发者可以重点关注三个流水任务的实现。

1. 进行**核函数的定义，** 并在核函数中调用算子类的Init和Process函数。

   ```
   1. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)
   2. {
   3. // 获取Host侧传入的Tiling参数
   4. GET_TILING_DATA(tiling_data, tiling);
   5. // 初始化算子类
   6. KernelAdd op;
   7. // 算子类的初始化函数，完成内存初始化相关工作
   8. op.Init(x, y, z, tiling_data.totalLength, tiling_data.tileNum);
   9. // 完成算子实现的核心逻辑
   10. op.Process();
   11. }
   ```
2. 定义KernelAdd算子类，其具体成员及成员函数实现如下。

   ```
   1. #include "kernel_operator.h"
   2. constexpr int32_t BUFFER_NUM = 2;
   3. class KernelAdd {
   4. public:
   5. __aicore__ inline KernelAdd() {}
   6. // 初始化函数，完成内存初始化相关操作
   7. __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z, uint32_t totalLength, uint32_t tileNum)
   8. {
   9. // 使用获取到的TilingData计算得到singleCoreSize(每个核上总计算数据大小)、tileNum（每个核上分块个数）、singleTileLength（每个分块大小）等变量
   10. this->blockLength = totalLength / AscendC::GetBlockNum();
   11. this->tileNum = tileNum;
   12. this->tileLength = this->blockLength / tileNum / BUFFER_NUM;

   14. // 获取当前核的起始索引
   15. xGm.SetGlobalBuffer((__gm__ DTYPE_X*)x + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
   16. yGm.SetGlobalBuffer((__gm__ DTYPE_Y*)y + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
   17. zGm.SetGlobalBuffer((__gm__ DTYPE_Z*)z + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
   18. // 通过Pipe内存管理对象为输入输出Queue分配内存
   19. pipe.InitBuffer(inQueueX, BUFFER_NUM, this->tileLength * sizeof(DTYPE_X));
   20. pipe.InitBuffer(inQueueY, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Y));
   21. pipe.InitBuffer(outQueueZ, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Z));
   22. }
   23. // 核心处理函数，实现算子逻辑，调用私有成员函数CopyIn、Compute、CopyOut完成矢量算子的三级流水操作
   24. __aicore__ inline void Process()
   25. {
   26. int32_t loopCount = this->tileNum * BUFFER_NUM;
   27. for (int32_t i = 0; i < loopCount; i++) {
   28. CopyIn(i);
   29. Compute(i);
   30. CopyOut(i);
   31. }
   32. }

   35. private:
   36. // 搬入函数，完成CopyIn阶段的处理，被核心Process函数调用
   37. __aicore__ inline void CopyIn(int32_t progress)
   38. {
   39. // 从Queue中分配输入Tensor
   40. AscendC::LocalTensor<DTYPE_X> xLocal = inQueueX.AllocTensor<DTYPE_X>();
   41. AscendC::LocalTensor<DTYPE_Y> yLocal = inQueueY.AllocTensor<DTYPE_Y>();
   42. // 将GlobalTensor数据拷贝到LocalTensor
   43. AscendC::DataCopy(xLocal, xGm[progress * this->tileLength], this->tileLength);
   44. AscendC::DataCopy(yLocal, yGm[progress * this->tileLength], this->tileLength);
   45. // 将LocalTensor放入VECIN（代表矢量编程中搬入数据的逻辑存放位置）的Queue中
   46. inQueueX.EnQue(xLocal);
   47. inQueueY.EnQue(yLocal);
   48. }
   49. // 计算函数，完成Compute阶段的处理，被核心Process函数调用
   50. __aicore__ inline void Compute(int32_t progress)
   51. {
   52. // 将Tensor从队列中取出，用于后续计算
   53. AscendC::LocalTensor<DTYPE_X> xLocal = inQueueX.DeQue<DTYPE_X>();
   54. AscendC::LocalTensor<DTYPE_Y> yLocal = inQueueY.DeQue<DTYPE_Y>();
   55. // 从Queue中分配输出Tensor
   56. AscendC::LocalTensor<DTYPE_Z> zLocal = outQueueZ.AllocTensor<DTYPE_Z>();
   57. // 调用Add接口进行计算
   58. AscendC::Add(zLocal, xLocal, yLocal, this->tileLength);
   59. // 将计算结果LocalTensor放入到VecOut的Queue中
   60. outQueueZ.EnQue<DTYPE_Z>(zLocal);
   61. // 释放输入Tensor
   62. inQueueX.FreeTensor(xLocal);
   63. inQueueY.FreeTensor(yLocal);
   64. }
   65. // 搬出函数，完成CopyOut阶段的处理，被核心Process函数调用
   66. __aicore__ inline void CopyOut(int32_t progress)
   67. {
   68. // 从VecOut的Queue中取出输出Tensor
   69. AscendC::LocalTensor<DTYPE_Z> zLocal = outQueueZ.DeQue<DTYPE_Z>();
   70. // 将输出Tensor拷贝到GlobalTensor中
   71. AscendC::DataCopy(zGm[progress * this->tileLength], zLocal, this->tileLength);
   72. // 将不再使用的LocalTensor释放
   73. outQueueZ.FreeTensor(zLocal);
   74. }

   77. private:
   78. // Pipe内存管理对象
   79. AscendC::TPipe pipe;
   80. // 输入数据Queue队列管理对象，QuePosition为VECIN
   81. AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueX, inQueueY;
   82. // 输出数据Queue队列管理对象，QuePosition为VECOUT
   83. AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueZ;
   84. // 管理输入输出Global Memory内存地址的对象，其中xGm, yGm为输入，zGm为输出
   85. AscendC::GlobalTensor<DTYPE_X> xGm;
   86. AscendC::GlobalTensor<DTYPE_Y> yGm;
   87. AscendC::GlobalTensor<DTYPE_Z> zGm;
   88. // 每个核上总计算数据大小
   89. uint32_t blockLength;
   90. // 每个核上总计算数据分块个数
   91. uint32_t tileNum;
   92. // 每个分块大小
   93. uint32_t tileLength;
   94. };
   ```

## Host侧算子实现

核函数开发并验证完成后，下一步就是进行Host侧的实现，对应“AddCustom/op\_host”目录下的add\_custom\_tiling.h文件与add\_custom.cpp文件。下面简要介绍下两个文件的关键实现，完整的样例代码可参见[add\_custom\_tiling.h](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/AddCustom/op_host/add_custom_tiling.h)与[add\_custom.cpp](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/AddCustom/op_host/add_custom.cpp)。

1. 修改“add\_custom\_tiling.h”文件，在此文件中增加粗体部分的代码，进行Tiling参数的定义。

   ```
   1. #ifndef ADD_CUSTOM_TILING_H
   2. #define ADD_CUSTOM_TILING_H
   3. #include "register/tilingdata_base.h"
   4. namespace optiling {
   5. BEGIN_TILING_DATA_DEF(AddCustomTilingData)
   6. // AddCustom算子使用了2个tiling参数：totalLength与tileNum
   7. TILING_DATA_FIELD_DEF(uint32_t, totalLength);     // 总计算数据量
   8. TILING_DATA_FIELD_DEF(uint32_t, tileNum);         // 每个核上总计算数据分块个数
   9. END_TILING_DATA_DEF;

   11. // 注册tiling数据到对应的算子
   12. REGISTER_TILING_DATA_CLASS(AddCustom, AddCustomTilingData)
   13. }
   14. #endif // ADD_CUSTOM_TILING_H
   ```
2. 修改“add\_custom.cpp”文件，进行Tiling的实现。

   修改“TilingFunc”函数，实现Tiling上下文的获取，并通过上下文获取输入输出shape信息，并根据shape信息设置TilingData，序列化保存TilingData，并设置TilingKey。

   ```
   1. namespace optiling {
   2. const uint32_t BLOCK_DIM = 1;
   3. const uint32_t TILE_NUM = 8;
   4. static ge::graphStatus TilingFunc(gert::TilingContext* context)
   5. {
   6. AddCustomTilingData tiling;
   7. uint32_t totalLength = context->GetInputShape(0)->GetOriginShape().GetShapeSize();
   8. context->SetBlockDim(BLOCK_DIM);
   9. tiling.set_totalLength(totalLength);
   10. tiling.set_tileNum(TILE_NUM);
   11. tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());
   12. context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());
   13. size_t *currentWorkspace = context->GetWorkspaceSizes(1);
   14. currentWorkspace[0] = 0;
   15. return ge::GRAPH_SUCCESS;
   16. }
   17. } // namespace optiling
   ```
3. 在“add\_custom.cpp”文件中实现AddCustom算子的shape推导。

   Add算子的输出shape等于输入shape，所以直接将输入shape赋给输出shape，当前msOpGen工具生成的代码“InferShape”函数无需修改。
4. 修改“add\_custom.cpp”文件中的算子原型注册，此函数为入口函数。

   ```
   1. namespace ops {
   2. class AddCustom : public OpDef {
   3. public:
   4. explicit AddCustom(const char* name) : OpDef(name)
   5. {
   6. // Add算子的第一个输入
   7. this->Input("x")
   8. .ParamType(REQUIRED)    // 代表输入必选
   9. .DataType({ ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32 })   // 输入支持的数据类型
   10. .Format({ ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND });   // 输入支持的数据格式
   11. // Add算子的第二个输入
   12. this->Input("y")
   13. .ParamType(REQUIRED)
   14. .DataType({ ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32 })
   15. .Format({ ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND });
   16. this->Output("z")
   17. .ParamType(REQUIRED)
   18. .DataType({ ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32 })
   19. .Format({ ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND });
   20. // 关联InferShape函数
   21. this->SetInferShape(ge::InferShape);
   22. // 关联Tiling函数
   23. this->AICore()
   24. .SetTiling(optiling::TilingFunc);
   25. // 注册算子支持的AI处理器型号，请替换为实际支持的AI处理器型号,如kirin9020
   26. this->AICore().AddConfig("kirinxxx");
   27. }
   28. };
   29. // 结束算子注册
   30. OP_ADD(AddCustom);
   31. } // namespace ops
   ```

## 算子工程编译部署

编译AddCustom工程，生成自定义算子安装包，并将其安装到算子库中。

1. 编译自定义算子工程，构建生成自定义算子包。

   在算子工程AddCustom目录下执行如下命令，进行算子工程编译。

   ```
   1. ./build.sh
   ```

   编译成功后，会在当前目录下创建build\_out目录，在build\_out/autogen目录下生成自定义算子交付件。
2. 自定义算子安装包部署。

   在执行编译的同时，会将交付件安装到DDK安装目录${DDK\_INSTALL\_PATH}下的指定目录。

   ```
   1. ${DDK_INSTALL_PATH}/tools/platform
   ```

   查看部署后的目录结构，如下所示：

   ```
   1. platform                            // 平台插件目录
   2. ├── kirin9020                       // Kirin AI处理器类型
   3. │   ├── config
   4. │   │   └── npu_custom_opinfo.json  // 算子信息库
   5. │   ├── lib64
   6. │   │   └── libcustom_op.so         // host侧二进制文件
   7. │   ├── ops
   8. │   │   └── impl
   9. │   │       ├── custom              // kernel交付件
   10. │   │       │   ├── add_custom.cpp
   11. │   │       │   ├── add_custom.py
   12. │   │       │   └── op_proto.h
   13. │   │       └── impl
   14. │   └── simulator
   15. └── README.md
   ```

---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-development
title: 快速入门
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > 快速入门
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bdc585950598bc003fd1e5c491253b3a2020da68a9a398664939af5b09603135
---

本节以一个简单算子为例，带开发者体验从算子工程创建、代码编写、编译部署到运行验证的开发全流程，让开发者对算子开发工程有个宏观的认识，此处我们以输入是动态shape的Add算子实现为例，为了与内置Add算子区分，定义算子类型为AddCustom。

## 工程创建

开发者可以基于鸿蒙CANN社区recipe仓提供的工程模板创建AscendC算子开发工程，模板中包含了算子实现的模板文件、编译脚本等。

1. 从鸿蒙CANN社区recipe仓获取算子工程模板，将仓内的样例单算子工程（如AddCustom算子，位于仓内"ops/ascendc/src/add\_custom"目录下）拷贝到本地目录（如$HOME/sample下），作为算子开发工程。

   ```shell
   git clone https://gitcode.com/cann/cann-recipes-harmony-infer.git
   cp -r ./cann-recipes-harmony-infer/ops/ascendc/src/add_custom $HOME/sample/AddCustom
   ```

   **说明** 

   鸿蒙CANN社区recipe仓的更多介绍请参见[仓工程模板说明](https://gitcode.com/cann/cann-recipes-harmony-infer/blob/master/README.md)。
2. 拷贝完成后，会在$HOME/sample目录下生成算子工程目录AddCustom，工程中包含算子实现的模板文件，编译脚本等，如下所示。

   ```text
   AddCustom
   ├── build_devices.sh // 开发者无需关注，在线编译场景预留，编译device侧交付件脚本
   ├── build.sh // 编译入口脚本
   ├── cmake
   │   ├── config.cmake
   │   ├── util // 算子工程编译所需脚本及公共编译文件存放目录
   ├── CMakeLists.txt // 算子工程的CMakeLists.txt
   ├── CMakePresets.json // 编译配置项
   ├── framework // 算子插件实现文件目录，单算子模型文件的生成不依赖算子适配插件，无需关注
   ├── op_host // host侧实现文件
   │   ├── add_custom_tiling.h // 算子tiling定义文件
   │   ├── add_custom.cpp // 算子原型注册、shape推导、信息库、tiling实现等内容文件
   │   ├── CMakeLists.txt
   ├── op_kernel // kernel侧实现文件
   │   ├── CMakeLists.txt
   │   ├── add_custom.cpp // 算子核函数实现文件
   ├── scripts // 自定义算子工程打包相关脚本所在目录
   ```

   **说明** 

   上述目录结构中的粗体文件op\_host/add\_custom\_tiling.h、op\_host/add\_custom.cpp、op\_kernel/add\_custom.cpp为后续算子开发过程中需要修改的文件，其他文件无需修改。样例工程的实际目录结构以仓内工程为准。

## 算子核函数实现

在工程存储目录的"AddCustom/op\_kernel/add\_custom.cpp"文件中实现算子的核函数，完整的样例代码开发者可以在[add\_custom.cpp](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/AddCustom/op_kernel/add_custom.cpp)中查看，下面介绍关键实现代码。

算子核函数实现代码的内部调用关系示意图如下。

**图1** 核函数调用关系图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Yn8TJLrhRGCbSLszTdII4Q/zh-cn_image_0000002786520604.png)

由此可见除了Init函数完成初始化外，Process中完成了对流水任务：搬入、计算、搬出的调用，开发者可以重点关注三个流水任务的实现。

1. 定义KernelAdd算子类，其具体成员及成员函数实现如下。

   ```cpp
   #include "kernel_operator.h"
   constexpr int32_t BUFFER_NUM = 2;
   class KernelAdd {
   public:
       __aicore__ inline KernelAdd() {}
       // 初始化函数，完成内存初始化相关操作
       __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z, uint32_t totalLength, uint32_t tileNum)
       {
           // 使用获取到的TilingData计算得到singleCoreSize(每个核上总计算数据大小)、tileNum（每个核上分块个数）、singleTileLength（每个分块大小）等变量
           this->blockLength = totalLength / AscendC::GetBlockNum();
           this->tileNum = tileNum;
           this->tileLength = this->blockLength / tileNum / BUFFER_NUM;
            
           // 获取当前核的起始索引
           xGm.SetGlobalBuffer((__gm__ DTYPE_X*)x + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
           yGm.SetGlobalBuffer((__gm__ DTYPE_Y*)y + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
           zGm.SetGlobalBuffer((__gm__ DTYPE_Z*)z + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
           // 通过Pipe内存管理对象为输入输出Queue分配内存
           pipe.InitBuffer(inQueueX, BUFFER_NUM, this->tileLength * sizeof(DTYPE_X));
           pipe.InitBuffer(inQueueY, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Y));
           pipe.InitBuffer(outQueueZ, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Z));
       }
       // 核心处理函数，实现算子逻辑，调用私有成员函数CopyIn、Compute、CopyOut完成矢量算子的三级流水操作
       __aicore__ inline void Process()
       {
           int32_t loopCount = this->tileNum * BUFFER_NUM;
           for (int32_t i = 0; i < loopCount; i++) {
               CopyIn(i);
               Compute(i);
               CopyOut(i);
           }
       }
    
    
   private:
       // 搬入函数，完成CopyIn阶段的处理，被核心Process函数调用
       __aicore__ inline void CopyIn(int32_t progress)
       {
           // 从Queue中分配输入Tensor
           AscendC::LocalTensor<DTYPE_X> xLocal = inQueueX.AllocTensor<DTYPE_X>();
           AscendC::LocalTensor<DTYPE_Y> yLocal = inQueueY.AllocTensor<DTYPE_Y>();
            // 将GlobalTensor数据拷贝到LocalTensor
           AscendC::DataCopy(xLocal, xGm[progress * this->tileLength], this->tileLength);
           AscendC::DataCopy(yLocal, yGm[progress * this->tileLength], this->tileLength);
           // 将LocalTensor放入VECIN（代表矢量编程中搬入数据的逻辑存放位置）的Queue中
           inQueueX.EnQue(xLocal);
           inQueueY.EnQue(yLocal);
       }
       // 计算函数，完成Compute阶段的处理，被核心Process函数调用
       __aicore__ inline void Compute(int32_t progress)
       {
           // 将Tensor从队列中取出，用于后续计算
           AscendC::LocalTensor<DTYPE_X> xLocal = inQueueX.DeQue<DTYPE_X>();
           AscendC::LocalTensor<DTYPE_Y> yLocal = inQueueY.DeQue<DTYPE_Y>();
           // 从Queue中分配输出Tensor
           AscendC::LocalTensor<DTYPE_Z> zLocal = outQueueZ.AllocTensor<DTYPE_Z>();
           // 调用Add接口进行计算
           AscendC::Add(zLocal, xLocal, yLocal, this->tileLength);
           // 将计算结果LocalTensor放入到VecOut的Queue中
           outQueueZ.EnQue<DTYPE_Z>(zLocal);
           // 释放输入Tensor
           inQueueX.FreeTensor(xLocal);
           inQueueY.FreeTensor(yLocal);
       }
       // 搬出函数，完成CopyOut阶段的处理，被核心Process函数调用
       __aicore__ inline void CopyOut(int32_t progress)
       {
           // 从VecOut的Queue中取出输出Tensor
           AscendC::LocalTensor<DTYPE_Z> zLocal = outQueueZ.DeQue<DTYPE_Z>();
           // 将输出Tensor拷贝到GlobalTensor中
           AscendC::DataCopy(zGm[progress * this->tileLength], zLocal, this->tileLength);
           // 将不再使用的LocalTensor释放
           outQueueZ.FreeTensor(zLocal);
       }
    
    
   private:
       // Pipe内存管理对象
       AscendC::TPipe pipe;
       // 输入数据Queue队列管理对象，QuePosition为VECIN
       AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueX, inQueueY;
       // 输出数据Queue队列管理对象，QuePosition为VECOUT
       AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueZ;
       // 管理输入输出Global Memory内存地址的对象，其中xGm, yGm为输入，zGm为输出
       AscendC::GlobalTensor<DTYPE_X> xGm;
       AscendC::GlobalTensor<DTYPE_Y> yGm;
       AscendC::GlobalTensor<DTYPE_Z> zGm;
       // 每个核上总计算数据大小
       uint32_t blockLength;
       // 每个核上总计算数据分块个数
       uint32_t tileNum;
       // 每个分块大小
       uint32_t tileLength;
   };
   ```
2. 进行**核函数的定义**并在核函数中调用算子类的Init和Process函数。

   ```cpp
   extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)
   {
       // 获取Host侧传入的Tiling参数
       GET_TILING_DATA(tiling_data, tiling);
       // 初始化算子类
       KernelAdd op;
       // 算子类的初始化函数，完成内存初始化相关工作
       op.Init(x, y, z, tiling_data.totalLength, tiling_data.tileNum);
       // 完成算子实现的核心逻辑
       op.Process();
   }
   ```

## Host侧算子实现

核函数开发并验证完成后，下一步就是进行Host侧的实现，对应“AddCustom/op\_host”目录下的add\_custom\_tiling.h文件与add\_custom.cpp文件。下面简要介绍下两个文件的关键实现，完整的样例代码可参见[add\_custom\_tiling.h](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/AddCustom/op_host/add_custom_tiling.h)与[add\_custom.cpp](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/AddCustom/op_host/add_custom.cpp)。

1. 修改“add\_custom\_tiling.h”文件，在此文件中增加粗体部分的代码，进行Tiling参数的定义。

   ```cpp
   #ifndef ADD_CUSTOM_TILING_H
   #define ADD_CUSTOM_TILING_H
   #include "register/tilingdata_base.h"
   namespace optiling {
   BEGIN_TILING_DATA_DEF(AddCustomTilingData)
     // AddCustom算子使用了2个tiling参数：totalLength与tileNum
     TILING_DATA_FIELD_DEF(uint32_t, totalLength); // 总计算数据量
     TILING_DATA_FIELD_DEF(uint32_t, tileNum); // 每个核上总计算数据分块个数
   END_TILING_DATA_DEF;
    
   // 注册tiling数据到对应的算子
   REGISTER_TILING_DATA_CLASS(AddCustom, AddCustomTilingData)
   }
   #endif // ADD_CUSTOM_TILING_H
   ```
2. 修改“add\_custom.cpp”文件，进行Tiling的实现。

   修改“TilingFunc”函数，实现Tiling上下文的获取，并通过上下文获取输入输出shape信息，并根据shape信息设置TilingData，序列化保存TilingData，并设置TilingKey。

   ```cpp
   namespace optiling {
   const uint32_t BLOCK_DIM = 1;
   const uint32_t TILE_NUM = 8;
   static ge::graphStatus TilingFunc(gert::TilingContext* context)
   {
       AddCustomTilingData tiling;
       uint32_t totalLength = context->GetInputShape(0)->GetOriginShape().GetShapeSize();
       context->SetBlockDim(BLOCK_DIM);
       tiling.set_totalLength(totalLength);
       tiling.set_tileNum(TILE_NUM);
       tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());
       context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());
       size_t *currentWorkspace = context->GetWorkspaceSizes(1);
       currentWorkspace[0] = 0;
       return ge::GRAPH_SUCCESS;
   }
   } // namespace optiling
   ```
3. 在“add\_custom.cpp”文件中实现AddCustom算子的shape推导。

   Add算子的输出shape等于输入shape，所以直接将输入shape赋给输出shape，工程模板中的“InferShape”函数无需修改。
4. 修改“add\_custom.cpp”文件中的算子原型注册，此函数为入口函数。

   ```cpp
   namespace ops {
   class AddCustom : public OpDef {
   public:
       explicit AddCustom(const char* name) : OpDef(name)
       {
           // Add算子的第一个输入
           this->Input("x")
               .ParamType(REQUIRED) // 代表输入必选
               .DataType({ ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32 }) // 输入支持的数据类型
               .Format({ ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND }); // 输入支持的数据格式
           // Add算子的第二个输入
           this->Input("y")
               .ParamType(REQUIRED)
               .DataType({ ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32 })
               .Format({ ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND });
           this->Output("z")
               .ParamType(REQUIRED)
               .DataType({ ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32 })
               .Format({ ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND });
           // 关联InferShape函数
           this->SetInferShape(ge::InferShape);
           // 关联Tiling函数
           this->AICore()
               .SetTiling(optiling::TilingFunc);
           // 注册算子支持的AI处理器型号，请替换为实际支持的AI处理器型号，如kirin9020
           this->AICore().AddConfig("kirinxxx");
       }
   };
   // 结束算子注册
   OP_ADD(AddCustom);
   } // namespace ops
   ```

## 算子工程编译部署

编译AddCustom工程，生成自定义算子安装包，并将其安装到算子库中。

1. 编译自定义算子工程，构建生成自定义算子包。

   在算子工程AddCustom目录下执行如下命令，进行算子工程编译。

   ```shell
   ./build.sh
   ```

   编译成功后，会在当前目录下创建build\_out目录，在build\_out/autogen目录下生成自定义算子交付件。
2. 自定义算子安装包部署。

   在执行编译的同时，会将交付件安装到DDK安装目录${DDK\_INSTALL\_PATH}下的指定目录。

   ```shell
   ${DDK_INSTALL_PATH}/tools/platform
   ```

   查看部署后的目录结构，如下所示：

   ```text
   platform // 平台插件目录
   ├── kirin9020 // Kirin AI处理器类型
   │   ├── config
   │   │   └── npu_custom_opinfo.json // 算子信息库
   │   ├── lib64
   │   │   └── libcustom_op.so // host侧二进制文件
   │   ├── ops
   │   │   └── impl
   │   │       ├── custom // kernel交付件
   │   │       │   ├── add_custom.cpp
   │   │       │   ├── add_custom.py
   │   │       │   └── op_proto.h
   │   │       └── impl
   │   └── simulator
   └── README.md
   ```

## 使用AI Agent完成算子开发

CANNBot是CANN社区为开发者提供的多智能体、端到端、自动化智能助手，支持代码自动生成，具备自主排障、闭环修复、端到端调优能力，有效降低开发者门槛。

其中，Ascend C注册算子开发插件(ops-registry-invoke)和Ascend C直调算子开发插件(ops-direct-invoke)均已支持Kirin平台。前者适用于生产级自定义算子开发场景，后者适用于算子的快速验证和原型开发或者Ascend C的学习。具体使用方式，详见[CANNBot仓](https://gitcode.com/cann/cannbot)。

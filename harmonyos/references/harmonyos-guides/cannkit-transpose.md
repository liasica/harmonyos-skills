---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-transpose
title: Transpose
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 数据转换 > Transpose
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:40e23784fbf2ff6a0b8510b891178b64ab060db32f2a87800b36041c9bc81b2d
---

## 功能说明

* 可实现16\*16的二维矩阵数据块的转置。
* 可实现[N, C, H, W]与[N, H, W, C]互相转换。

## 函数原型

* 普通转置，支持16\*16的二维矩阵数据块进行转置

  ```cpp
  template <typename T> 
  void Transpose(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal)
  ```
* 增强转置，支持16\*16的二维矩阵数据块转置，支持[N, C, H, W]与[N, H, W, C]互相转换

  ```cpp
  template <typename T> 
  void Transpose(const LocalTensor<T> &dstLocal, const LocalTensor<T> &srcLocal, const LocalTensor<uint8_t> &sharedTmpBuffer, const TransposeParamsExt &transposeParams)
  ```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数的数据类型。  **普通转置接口：**  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、int16\_t、uint16\_t  **增强转置接口：**  参考表4。 |

**表2** 接口参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。 |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  数据类型需要与dstLocal保持一致。 |
| sharedTmpBuffer | 输入 | 共享的临时Buffer Tensor，sharedTmpBuffer的大小参考表5。 |
| transposeParams | 输入 | 控制Transpose的数据结构。结构体内包含：输入的shape信息和transposeType参数。该数据结构的定义请参考表3。 |

**表3** transposeParams结构体内参数说明

| 参数名称 | 含义 |
| --- | --- |
| nSize | n轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| cSize | c轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| hSize | h轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| wSize | w轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| transposeType | 数据排布及reshape的类型，类型为TransposeType枚举类。具体取值为：TRANSPOSE\_TYPE\_NONE、TRANSPOSE\_ND2ND\_B16、TRANSPOSE\_NCHW2NHWC、TRANSPOSE\_NHWC2NCHW；  当前预留参数，暂不支持：TRANSPOSE\_NZ2ND\_0213、TRANSPOSE\_NZ2NZ\_0213、TRANSPOSE\_NZ2NZ\_012\_WITH\_N、TRANSPOSE\_NZ2ND\_012\_WITH\_N、TRANSPOSE\_NZ2ND\_012\_WITHOUT\_N、TRANSPOSE\_NZ2NZ\_012\_WITHOUT\_N、TRANSPOSE\_ND2ND\_ONLY、TRANSPOSE\_ND\_UB\_GM、TRANSPOSE\_GRAD\_ND\_UB\_GM。  **说明：** 当transposeType为TRANSPOSE\_ND2ND\_B16时，hSize和wSize必须传入16，nSize和cSize传入无效。 |

**表4** 增强转置接口支持的数据类型

| transposeType | 支持的数据类型 |
| --- | --- |
| TRANSPOSE\_ND2ND\_B16 | 无 |
| TRANSPOSE\_NCHW2NHWC | Kirin X90系列处理器，操作数支持的数据类型为：int8\_t、uint8\_t、int16\_t、uint16\_t、half、int32\_t、uint32\_t、float。  Kirin 9020系列处理器，操作数支持的数据类型为：int8\_t、uint8\_t、int16\_t、uint16\_t、half、int32\_t、uint32\_t、float。 |
| TRANSPOSE\_NHWC2NCHW | Kirin X90系列处理器，操作数支持的数据类型为：int8\_t、uint8\_t、int16\_t、uint16\_t、half、int32\_t、uint32\_t、float。  Kirin 9020系列处理器，操作数支持的数据类型为：int8\_t、uint8\_t、int16\_t、uint16\_t、half、int32\_t、uint32\_t、float。 |

**表5** 增强转置接口sharedTmpBuffer所需的大小

| transposeType | sharedTmpBuffer所需的大小 |
| --- | --- |
| TRANSPOSE\_ND2ND\_B16 | 不需要临时Buffer。 |
| TRANSPOSE\_NCHW2NHWC | 临时Buffer的大小按照下述计算规则（伪代码）进行计算。  auto h0 = 16; // 当数据类型的位宽为8时，h0 = 32；其他情况下，h0 = 16  auto w0 = 32 / sizeof(type); // type代表数据类型  auto tmpBufferSize = (cSize + 2) \* h0 \* w0 \* sizeof(type); |
| TRANSPOSE\_NHWC2NCHW | 临时Buffer的大小按照下述计算规则（伪代码）进行计算。  auto h0 = 16; // 当数据类型的位宽为8时，h0 = 32；其他情况下，h0 = 16  auto w0 = 32 / sizeof(type); // type代表数据类型  auto tmpBufferSize = (cSize \* 2 + 1) \* h0 \* w0 \* sizeof(type); |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* 该指令不可迭代（即不能通过repeatTimes重复）。
* [N, C, H, W]与[N, H, W, C]互相转换，H \* W需要32B对齐。
* 普通转置接口支持srcLocal和dstLocal复用。
* 增强转置接口，transposeType为TRANSPOSE\_ND2ND\_B16时支持srcLocal和dstLocal复用，transposeType为TRANSPOSE\_NCHW2NHWC、TRANSPOSE\_NHWC2NCHW时不支持srcLocal和dstLocal复用。

## 返回值

无

## 调用示例

* 普通接口调用示例，该示例对[16, 16]的half类型矩阵进行转置。

  ```cpp
  #include "kernel_operator.h"
    
   class KernelTranspose {
   public:
       __aicore__ inline KernelTranspose() {}
       __aicore__ inline void Init(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
       {
           srcGlobal.SetGlobalBuffer((__gm__ half*)src);
           dstGlobal.SetGlobalBuffer((__gm__ half*)dstGm);
    
           pipe.InitBuffer(inQueueSrc, 1, srcDataSize * sizeof(half));
           pipe.InitBuffer(outQueueDst, 1, dstDataSize * sizeof(half));
       }
       __aicore__ inline void Process()
       {
           CopyIn();
           Compute();
           CopyOut();
       }
   private:
       __aicore__ inline void CopyIn()
       {
           AscendC::LocalTensor<half> srcLocal = inQueueSrc.AllocTensor<half>();
           AscendC::DataCopy(srcLocal, srcGlobal, srcDataSize);
           inQueueSrc.EnQue(srcLocal);
       }
       __aicore__ inline void Compute()
       {
           AscendC::LocalTensor<half> srcLocal = inQueueSrc.DeQue<half>();
           AscendC::LocalTensor<half> dstLocal = outQueueDst.AllocTensor<half>();
    
           AscendC::Transpose<half>(dstLocal, srcLocal);
    
           outQueueDst.EnQue<half>(dstLocal);
           inQueueSrc.FreeTensor(srcLocal);
       }
       __aicore__ inline void CopyOut()
       {
           AscendC::LocalTensor<half> dstLocal = outQueueDst.DeQue<half>();
           AscendC::DataCopy(dstGlobal, dstLocal, dstDataSize);
           outQueueDst.FreeTensor(dstLocal);
       }
   private:
       AscendC::TPipe pipe;
       AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
       AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    
       AscendC::GlobalTensor<half> srcGlobal, dstGlobal;
       int srcDataSize = 256;
       int dstDataSize = 256;
   };
    
   extern "C" __global__ __aicore__ void transpose_kernel(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
   {
       KernelTranspose op;
       op.Init(src, dstGm);
       op.Process();
   }
  ```

  ```text
  输入数据(src_gm):
   [[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.
      14.  15.]
    [ 16.  17.  18.  19.  20.  21.  22.  23.  24.  25.  26.  27.  28.  29.
      30.  31.]
    [ 32.  33.  34.  35.  36.  37.  38.  39.  40.  41.  42.  43.  44.  45.
      46.  47.]
    [ 48.  49.  50.  51.  52.  53.  54.  55.  56.  57.  58.  59.  60.  61.
      62.  63.]
    [ 64.  65.  66.  67.  68.  69.  70.  71.  72.  73.  74.  75.  76.  77.
      78.  79.]
    [ 80.  81.  82.  83.  84.  85.  86.  87.  88.  89.  90.  91.  92.  93.
      94.  95.]
    [ 96.  97.  98.  99. 100. 101. 102. 103. 104. 105. 106. 107. 108. 109.
     110. 111.]
    [112. 113. 114. 115. 116. 117. 118. 119. 120. 121. 122. 123. 124. 125.
     126. 127.]
    [128. 129. 130. 131. 132. 133. 134. 135. 136. 137. 138. 139. 140. 141.
     142. 143.]
    [144. 145. 146. 147. 148. 149. 150. 151. 152. 153. 154. 155. 156. 157.
     158. 159.]
    [160. 161. 162. 163. 164. 165. 166. 167. 168. 169. 170. 171. 172. 173.
     174. 175.]
    [176. 177. 178. 179. 180. 181. 182. 183. 184. 185. 186. 187. 188. 189.
     190. 191.]
    [192. 193. 194. 195. 196. 197. 198. 199. 200. 201. 202. 203. 204. 205.
     206. 207.]
    [208. 209. 210. 211. 212. 213. 214. 215. 216. 217. 218. 219. 220. 221.
     222. 223.]
    [224. 225. 226. 227. 228. 229. 230. 231. 232. 233. 234. 235. 236. 237.
     238. 239.]
    [240. 241. 242. 243. 244. 245. 246. 247. 248. 249. 250. 251. 252. 253.
     254. 255.]]
    
  输出数据(dst_gm):
   [[  0.  16.  32.  48.  64.  80.  96. 112. 128. 144. 160. 176. 192. 208.
     224. 240.]
    [  1.  17.  33.  49.  65.  81.  97. 113. 129. 145. 161. 177. 193. 209.
     225. 241.]
    [  2.  18.  34.  50.  66.  82.  98. 114. 130. 146. 162. 178. 194. 210.
     226. 242.]
    [  3.  19.  35.  51.  67.  83.  99. 115. 131. 147. 163. 179. 195. 211.
     227. 243.]
    [  4.  20.  36.  52.  68.  84. 100. 116. 132. 148. 164. 180. 196. 212.
     228. 244.]
    [  5.  21.  37.  53.  69.  85. 101. 117. 133. 149. 165. 181. 197. 213.
     229. 245.]
    [  6.  22.  38.  54.  70.  86. 102. 118. 134. 150. 166. 182. 198. 214.
     230. 246.]
    [  7.  23.  39.  55.  71.  87. 103. 119. 135. 151. 167. 183. 199. 215.
     231. 247.]
    [  8.  24.  40.  56.  72.  88. 104. 120. 136. 152. 168. 184. 200. 216.
     232. 248.]
    [  9.  25.  41.  57.  73.  89. 105. 121. 137. 153. 169. 185. 201. 217.
     233. 249.]
    [ 10.  26.  42.  58.  74.  90. 106. 122. 138. 154. 170. 186. 202. 218.
     234. 250.]
    [ 11.  27.  43.  59.  75.  91. 107. 123. 139. 155. 171. 187. 203. 219.
     235. 251.]
    [ 12.  28.  44.  60.  76.  92. 108. 124. 140. 156. 172. 188. 204. 220.
     236. 252.]
    [ 13.  29.  45.  61.  77.  93. 109. 125. 141. 157. 173. 189. 205. 221.
     237. 253.]
    [ 14.  30.  46.  62.  78.  94. 110. 126. 142. 158. 174. 190. 206. 222.
     238. 254.]
    [ 15.  31.  47.  63.  79.  95. 111. 127. 143. 159. 175. 191. 207. 223.
     239. 255.]]
  ```
* 增强接口调用示例，完成half类型的[N, C, H, W]->[N, H, W, C]转置。

  ```cpp
  #include "kernel_operator.h"
    
   template <typename T> 
   class Kernel4dTrans {
   public:
       __aicore__ inline Kernel4dTrans() {}
       __aicore__ inline void Init(__gm__ uint8_t *srcGm, __gm__ uint8_t *dstGm)
       {
           inputSize = N * C * H * W;
           tmpBufferSize = (C + 2) * 16 * 16;
           srcGlobal.SetGlobalBuffer((__gm__ T *)srcGm);
           dstGlobal.SetGlobalBuffer((__gm__ T *)dstGm);
           pipe.InitBuffer(inQueueSrcVecIn, 1, inputSize*sizeof(T));
           pipe.InitBuffer(inQueueSrcVecOut, 1, inputSize*sizeof(T));
           pipe.InitBuffer(tmpQueue, 1, tmpBufferSize * sizeof(T));
       }
       __aicore__ inline void Process()
       {
           CopyIn();
           Compute();
           CopyOut();
       }
   private:
       __aicore__ inline void CopyIn()
       {
           AscendC::LocalTensor<T> srcLocal = inQueueSrcVecIn.AllocTensor<T>();
           AscendC::DataCopy(srcLocal, srcGlobal, inputSize);
           inQueueSrcVecIn.EnQue(srcLocal);
       }
       __aicore__ inline void Compute()
       {
           AscendC::LocalTensor<T> srcLocal = inQueueSrcVecIn.DeQue<T>();
           AscendC::LocalTensor<T> dstLocal = inQueueSrcVecOut.AllocTensor<T>();
           AscendC::LocalTensor<uint8_t> stackBuffer = tmpQueue.AllocTensor<uint8_t>();
    
           AscendC::TransposeParamsExt transposeParams;
           transposeParams.nSize = N;
           transposeParams.cSize = C;
           transposeParams.hSize = H;
           transposeParams.wSize = W;
           transposeParams.transposeType = transposetype;
           AscendC::Transpose(dstLocal, srcLocal, stackBuffer, transposeParams);
           inQueueSrcVecOut.EnQue<T>(dstLocal);
           inQueueSrcVecIn.FreeTensor(srcLocal);
           tmpQueue.FreeTensor(stackBuffer);
       }
       __aicore__ inline void CopyOut()
       {
           AscendC::LocalTensor<T> dstLocal = inQueueSrcVecOut.DeQue<T>();
           AscendC::DataCopy(dstGlobal, dstLocal, inputSize);
           inQueueSrcVecOut.FreeTensor(dstLocal);
       }
   private:
       AscendC::TPipe pipe;
       AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrcVecIn;
       AscendC::TQue<AscendC::QuePosition::VECOUT, 1> inQueueSrcVecOut;
       AscendC::TQue<AscendC::QuePosition::VECCALC, 1> tmpQueue;
    
       AscendC::GlobalTensor<T> srcGlobal;
       AscendC::GlobalTensor<T> dstGlobal;
       uint32_t N = 3;
       uint32_t C = 3;
       uint32_t H = 2;
       uint32_t W = 8;
       uint32_t inputSize, tmpBufferSize;
       AscendC::TransposeType transposetype = AscendC::TransposeType::TRANSPOSE_NCHW2NHWC;
   };
    
   extern "C" __global__ __aicore__ void transpose_kernel(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
   {
       Kernel4dTrans<half>op;
       op.Init(srcGm, dstGm);
       op.Process();
   }
  ```

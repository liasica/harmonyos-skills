---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hitss-api-ref
title: HiTSS
breadcrumb: API参考 > 标准库 > HiTSS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8c6b9bf33fabf12d0ef16c564441ea6180f51dc76c56ee7fc911a9447a7092ec
---

## 简介

HiTSS是基于TPM（Trusted Platform Module）2.0规范开发的组件，它提供了访问TPM 2.0芯片的API，包括命令传输接口、系统级接口和序列化反序列化接口，使开发者可以更方便地使用TPM 2.0芯片用于执行各种TPM操作，例如创建密钥、签名验签等，帮助开发者轻松与TPM 2.0芯片进行通信。HiTSS目前只针对鸿蒙电脑企业客户开放。

## HiTSS版本

从API 6.0.0(20)开始，HiTSS匹配TCG （Trusted Computing Group）TSS（TPM2 Software Stack）规范版本为：

* TCG TSS 2.0 Overview and Common Structures Specification Version 1.0 Revision 10, September 23 2021
* TCG TSS 2.0 Marshaling/Unmarshaling API Specification Version 1.0 Revision 07, 10 March 2020
* TCG TSS 2.0 System Level API (SAPI) Specification Version 1.1 Revision 36, October 1 2021
* TCG TSS 2.0 TPM Command Transmission Interface (TCTI) API Specification Version 1.0 Revision 18, 24 January 2020

## HiTSS支持的能力

* 命令传输接口，具体内容请参见[HiTSS支持的命令传输接口列表](hitss-api-ref.md#hitss支持的命令传输接口列表)。
* 序列化反序列化接口，具体内容请参见[HiTSS支持的序列化和反序列化接口列表](hitss-api-ref.md#hitss支持的序列化和反序列化接口列表)。
* 系统级接口（由于芯片能力限制，HiTSS只支持部分系统级接口），具体内容请参见[HiTSS支持的系统级接口列表](hitss-api-ref.md#hitss支持的系统级接口列表)。

## 引入HiTSS能力

1. 开发应用时，在访问命令传输接口或系统级接口前，需要申请权限：ohos.permission.CALL\_TPM\_CMD，申请方式请参考：[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。
2. 如果开发者需要使用HiTSS相关能力，首先请添加头文件。

   ```
   1. #include <tss2/tss2_common.h>
   2. #include <tss2/tss2_tpm2_types.h>
   3. #include <tss2/tss2_mu.h>
   4. #include <tss2/tss2_sys.h>
   5. #include <tss2/tss2_tcti.h>
   6. #include <tss2/tss2_tctildr.h>
   ```
3. 其次在CMakeLists.txt中添加以下动态链接库。

   ```
   1. libtss2-mu.so
   2. libtss2-sys.so
   3. libtss2-tctildr.so
   ```

## 使用示例

```
1. #include <stdio.h>
2. #include <tss2/tss2_tctildr.h>
3. #include <tss2/tss2_sys.h>
4. #include <tss2/tss2_mu.h>

6. #define SAFE_FREE(p) do { \
7. if ((p) != NULL) { \
8. free(p); \
9. (p) = NULL; \
10. } \
11. } while (false)

13. // 初始化上下文
14. TSS2_SYS_CONTEXT* InitSysCtx()
15. {
16. TSS2_TCTI_CONTEXT *tctiCtx = NULL;
17. const char *nameConf = "hmsa";
18. // nameConf参数字符串中不支持设定conf，conf必须为空
19. // 正确用法
20. // Tss2_TctiLdr_Initialize("hmsa", &tctiCtx);
21. // Tss2_TctiLdr_Initialize("hmsa:", &tctiCtx);
22. // 错误用法
23. // Tss2_TctiLdr_Initialize("hmsa:/dev/tpm0", &tctiCtx);
24. TSS2_RC rc = Tss2_TctiLdr_Initialize(nameConf, &tctiCtx);
25. if (rc != TSS2_RC_SUCCESS) {
26. return NULL;
27. }
28. size_t size = Tss2_Sys_GetContextSize(0);
29. TSS2_SYS_CONTEXT *sysCtx = (TSS2_SYS_CONTEXT *)calloc(1, size);
30. if (sysCtx == nullptr) {
31. return NULL;
32. }
33. TSS2_ABI_VERSION ver = TSS2_ABI_VERSION_CURRENT;
34. rc = Tss2_Sys_Initialize(sysCtx, size, tctiCtx, &ver);
35. if (rc != TSS2_RC_SUCCESS) {
36. Tss2_TctiLdr_Finalize(&tctiCtx);
37. SAFE_FREE(sysCtx);
38. return NULL;
39. }
40. return sysCtx;
41. }

43. // 释放上下文
44. void ReleaseSysCtx(TSS2_SYS_CONTEXT **sysCtx)
45. {
46. TSS2_TCTI_CONTEXT *tctiCtx = NULL;
47. TSS2_RC rc = Tss2_Sys_GetTctiContext(*sysCtx, &tctiCtx);
48. if (rc != TSS2_RC_SUCCESS) {
49. return;
50. }
51. if (tctiCtx != NULL) {
52. Tss2_TctiLdr_Finalize(&tctiCtx);
53. }
54. Tss2_Sys_Finalize(*sysCtx);
55. SAFE_FREE(*sysCtx);
56. }

58. // 通过Sys API获取随机数示例
59. void GetRandomExample()
60. {
61. TSS2_SYS_CONTEXT *sysCtx = InitSysCtx();
62. if (sysCtx == NULL) {
63. return;
64. }
65. TPM2B_DIGEST random = {};
66. TSS2_RC rc = Tss2_Sys_GetRandom(sysCtx, NULL, 32, &random, NULL); // 32: 随机数长度
67. if (rc != TSS2_RC_SUCCESS) {
68. printf("Failed to get random, error:%d.\n", rc);
69. }
70. ReleaseSysCtx(&sysCtx);
71. }

73. // 通过Sys API获取随机数示例
74. void GetRandomExample2()
75. {
76. TSS2_SYS_CONTEXT *sysCtx = InitSysCtx();
77. if (sysCtx == NULL) {
78. return;
79. }
80. TPM2B_DIGEST random = {};
81. do {
82. if (Tss2_Sys_GetRandom_Prepare(sysCtx, 32) != TSS2_RC_SUCCESS) { // 32: 随机数长度
83. break;
84. }
85. if (Tss2_Sys_Execute(sysCtx) != TSS2_RC_SUCCESS) {
86. break;
87. }
88. if (Tss2_Sys_GetRandom_Complete(sysCtx, &random) != TSS2_RC_SUCCESS) {
89. break;
90. }
91. } while(false);
92. ReleaseSysCtx(&sysCtx);
93. }

95. // MU API使用示例
96. void Int32MarshalUnmarshalExample()
97. {
98. INT32 data = 20;
99. uint8_t buffer[sizeof(data)] = { 0 };
100. size_t bufferSize = sizeof(data);
101. // 序列化data
102. TSS2_RC rc = Tss2_MU_INT32_Marshal(data, buffer, bufferSize, NULL);
103. if (rc != TSS2_RC_SUCCESS) {
104. printf("Failed to marshal data, error:%d.\n", rc);
105. }
106. INT32 dest = 0;
107. // 反序列化data，然后打印
108. rc = Tss2_MU_INT32_Unmarshal(buffer, bufferSize, NULL, &dest);
109. if (rc != TSS2_RC_SUCCESS) {
110. printf("Failed to unmarshal data, error:%d.\n", rc);
111. }
112. printf("The unmarshal result is %d.\n", dest);
113. }
```

## 错误码

说明

以下仅介绍HiTSS特有错误码，通用错误码请参考[TCG TSS 2.0 Overview and Common Structures Specification](https://trustedcomputinggroup.org/wp-content/uploads/TSS_Overview_Common_v1_r10_pub09232021.pdf)。

### TSS2\_BASE\_RC\_INTERNAL\_ERROR

**错误描述**

内部错误。

**可能原因**

代码内部处理逻辑与预期不符。

**处理步骤**

检查代码逻辑和芯片状态是否正确。

### TSS2\_BASE\_RC\_SAPI\_INIT

**错误描述**

SAPI上下文初始化失败。

**可能原因**

参数不正确。

**处理步骤**

检查函数入参是否正确。

### TSS2\_BASE\_RC\_CANCEL

**错误描述**

命令取消错误。

**可能原因**

命令队列已满。

**处理步骤**

尝试重试。

### TSS2\_TCTI\_RC\_MEMORY

**错误描述**

TCTI接口内存错误。

**可能原因**

设备内存不足或其它内存异常。

**处理步骤**

查看设备可用内存是否大于申请内存，并及时清理设备内存。

## 与TCG TSS标准规范的差异

以下类型和结构体与TCG TSS标准规范存在差异，HiTSS在标准规范基础上进行了能力扩充和错误修复。

```
1. // HiTSS新增宏定义
2. #define TPM2_ST_ATTEST_NV_DIGEST ((TPM2_ST) 0x801C)

4. // HiTSS新增nvDigest字段
5. typedef union TPMU_ATTEST TPMU_ATTEST;
6. union TPMU_ATTEST {
7. TPMS_CERTIFY_INFO certify; /* TPM2_ST_ATTEST_CERTIFY */
8. TPMS_CREATION_INFO creation; /* TPM2_ST_ATTEST_CREATION */
9. TPMS_QUOTE_INFO quote; /* TPM2_ST_ATTEST_QUOTE */
10. TPMS_COMMAND_AUDIT_INFO commandAudit; /* TPM2_ST_ATTEST_COMMAND_AUDIT */
11. TPMS_SESSION_AUDIT_INFO sessionAudit; /* TPM2_ST_ATTEST_SESSION_AUDIT */
12. TPMS_TIME_ATTEST_INFO time; /* TPM2_ST_ATTEST_TIME */
13. TPMS_NV_CERTIFY_INFO nv; /* TPM2_ST_ATTEST_NV */
14. TPMS_NV_DIGEST_CERTIFY_INFO nvDigest; /* TPM2_ST_ATTEST_NV_DIGEST */
15. };

17. // HiTSS新增类型
18. typedef TPM2_KEY_BITS TPMI_TDES_KEY_BITS;

20. // HiTSS新增tdes字段
21. typedef union TPMU_SYM_KEY_BITS TPMU_SYM_KEY_BITS;
22. union TPMU_SYM_KEY_BITS {
23. TPMI_TDES_KEY_BITS tdes; /* TPM2_ALG_TDES */
24. TPMI_AES_KEY_BITS aes; /* TPM2_ALG_AES */
25. TPMI_SM4_KEY_BITS sm4; /* TPM2_ALG_SM4 */
26. TPMI_CAMELLIA_KEY_BITS camellia; /* TPM2_ALG_CAMELLIA */
27. TPM2_KEY_BITS sym;
28. TPMI_ALG_HASH exclusiveOr; /* TPM2_ALG_XOR */
29. TPMS_EMPTY null; /* TPM2_ALG_NULL */
30. };

32. // HiTSS新增tdes字段
33. typedef union TPMU_SYM_MODE TPMU_SYM_MODE;
34. union TPMU_SYM_MODE {
35. TPMI_ALG_SYM_MODE tdes; /* TPM2_ALG_TDES */
36. TPMI_ALG_SYM_MODE aes; /* TPM2_ALG_AES */
37. TPMI_ALG_SYM_MODE sm4; /* TPM2_ALG_SM4 */
38. TPMI_ALG_SYM_MODE camellia; /* TPM2_ALG_CAMELLIA */
39. TPMI_ALG_SYM_MODE sym;
40. TPMS_EMPTY exclusiveOr; /* TPM2_ALG_XOR */
41. TPMS_EMPTY null; /* TPM2_ALG_NULL */
42. };

44. // TCG规范中缺失的定义
45. typedef UINT32 TPM2_AT;

47. // TCG规范中缺失的定义
48. #define TPM2_MAX_AC_CAPABILITIES (TPM2_MAX_CAP_BUFFER / sizeof(TPMS_AC_OUTPUT))

50. // 为方便用户使用，HiTSS新增TPM2B结构体
51. typedef struct {
52. UINT16 size;
53. BYTE buffer[];
54. } TPM2B;

56. // TCG规范中缺失的定义
57. typedef TPM2_HANDLE TPMI_RH_HIERARCHY_POLICY;

59. // TCG规范中错误定义了tag字段的类型，HiTSS进行了修正
60. typedef struct TPMS_AC_OUTPUT TPMS_AC_OUTPUT;
61. struct TPMS_AC_OUTPUT {
62. TPM2_AT tag;
63. UINT32 data;
64. };
```

## 相关参考

* [TCG TSS 2.0 Marshaling/Unmarshaling API Specification](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TSS_Marshaling_Unmarshaling_API_v1p0_r07_pub.pdf)
* [TCG TSS 2.0 System Level API (SAPI) Specification](https://trustedcomputinggroup.org/wp-content/uploads/TSS_SAPI_v1p1_r36_pub10012021.pdf)
* [TCG TSS 2.0 TPM Command Transmission Interface (TCTI) API Specification](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TSS_TCTI_v1p0_r18_pub.pdf)
* [TCG TSS 2.0 Overview and Common Structures Specification](https://trustedcomputinggroup.org/wp-content/uploads/TSS_Overview_Common_v1_r10_pub09232021.pdf)

## HiTSS支持的系统级接口列表

### 命令上下文管理

* Tss2\_Sys\_GetContextSize
* Tss2\_Sys\_Initialize
* Tss2\_Sys\_Finalize
* Tss2\_Sys\_GetTctiContext

### 命令准备

* Tss2\_Sys\_SetCmdAuths

### 命令执行

* Tss2\_Sys\_ExecuteAsync
* Tss2\_Sys\_ExecuteFinish
* Tss2\_Sys\_Execute
* Tss2\_Sys\_GetRspAuths

### TPM命令调用

| Prepare接口 | Complete接口 | 命令接口 |
| --- | --- | --- |
| Tss2\_Sys\_Startup\_Prepare | Tss2\_Sys\_Startup\_Complete | Tss2\_Sys\_Startup |
| Tss2\_Sys\_Shutdown\_Prepare | Tss2\_Sys\_Shutdown\_Complete | Tss2\_Sys\_Shutdown |
| Tss2\_Sys\_SelfTest\_Prepare | Tss2\_Sys\_SelfTest\_Complete | Tss2\_Sys\_SelfTest |
| Tss2\_Sys\_IncrementalSelfTest\_Prepare | Tss2\_Sys\_IncrementalSelfTest\_Complete | Tss2\_Sys\_IncrementalSelfTest |
| Tss2\_Sys\_GetTestResult\_Prepare | Tss2\_Sys\_GetTestResult\_Complete | Tss2\_Sys\_GetTestResult |
| Tss2\_Sys\_StartAuthSession\_Prepare | Tss2\_Sys\_StartAuthSession\_Complete | Tss2\_Sys\_StartAuthSession |
| Tss2\_Sys\_PolicyRestart\_Prepare | Tss2\_Sys\_PolicyRestart\_Complete | Tss2\_Sys\_PolicyRestart |
| Tss2\_Sys\_Create\_Prepare | Tss2\_Sys\_Create\_Complete | Tss2\_Sys\_Create |
| Tss2\_Sys\_Load\_Prepare | Tss2\_Sys\_Load\_Complete | Tss2\_Sys\_Load |
| Tss2\_Sys\_LoadExternal\_Prepare | Tss2\_Sys\_LoadExternal\_Complete | Tss2\_Sys\_LoadExternal |
| Tss2\_Sys\_ReadPublic\_Prepare | Tss2\_Sys\_ReadPublic\_Complete | Tss2\_Sys\_ReadPublic |
| Tss2\_Sys\_ActivateCredential\_Prepare | Tss2\_Sys\_ActivateCredential\_Complete | Tss2\_Sys\_ActivateCredential |
| Tss2\_Sys\_MakeCredential\_Prepare | Tss2\_Sys\_MakeCredential\_Complete | Tss2\_Sys\_MakeCredential |
| Tss2\_Sys\_Unseal\_Prepare | Tss2\_Sys\_Unseal\_Complete | Tss2\_Sys\_Unseal |
| Tss2\_Sys\_ObjectChangeAuth\_Prepare | Tss2\_Sys\_ObjectChangeAuth\_Complete | Tss2\_Sys\_ObjectChangeAuth |
| Tss2\_Sys\_CreateLoaded\_Prepare | Tss2\_Sys\_CreateLoaded\_Complete | Tss2\_Sys\_CreateLoaded |
| Tss2\_Sys\_Duplicate\_Prepare | Tss2\_Sys\_Duplicate\_Complete | Tss2\_Sys\_Duplicate |
| Tss2\_Sys\_Rewrap\_Prepare | Tss2\_Sys\_Rewrap\_Complete | Tss2\_Sys\_Rewrap |
| Tss2\_Sys\_Import\_Prepare | Tss2\_Sys\_Import\_Complete | Tss2\_Sys\_Import |
| Tss2\_Sys\_RSA\_Encrypt\_Prepare | Tss2\_Sys\_RSA\_Encrypt\_Complete | Tss2\_Sys\_RSA\_Encrypt |
| Tss2\_Sys\_RSA\_Decrypt\_Prepare | Tss2\_Sys\_RSA\_Decrypt\_Complete | Tss2\_Sys\_RSA\_Decrypt |
| Tss2\_Sys\_ECDH\_KeyGen\_Prepare | Tss2\_Sys\_ECDH\_KeyGen\_Complete | Tss2\_Sys\_ECDH\_KeyGen |
| Tss2\_Sys\_ECDH\_ZGen\_Prepare | Tss2\_Sys\_ECDH\_ZGen\_Complete | Tss2\_Sys\_ECDH\_ZGen |
| Tss2\_Sys\_ECC\_Parameters\_Prepare | Tss2\_Sys\_ECC\_Parameters\_Complete | Tss2\_Sys\_ECC\_Parameters |
| Tss2\_Sys\_ZGen\_2Phase\_Prepare | Tss2\_Sys\_ZGen\_2Phase\_Complete | Tss2\_Sys\_ZGen\_2Phase |
| Tss2\_Sys\_EncryptDecrypt\_Prepare | Tss2\_Sys\_EncryptDecrypt\_Complete | Tss2\_Sys\_EncryptDecrypt |
| Tss2\_Sys\_EncryptDecrypt2\_Prepare | Tss2\_Sys\_EncryptDecrypt2\_Complete | Tss2\_Sys\_EncryptDecrypt2 |
| Tss2\_Sys\_Hash\_Prepare | Tss2\_Sys\_Hash\_Complete | Tss2\_Sys\_Hash |
| Tss2\_Sys\_HMAC\_Prepare | Tss2\_Sys\_HMAC\_Complete | Tss2\_Sys\_HMAC |
| Tss2\_Sys\_GetRandom\_Prepare | Tss2\_Sys\_GetRandom\_Complete | Tss2\_Sys\_GetRandom |
| Tss2\_Sys\_StirRandom\_Prepare | Tss2\_Sys\_StirRandom\_Complete | Tss2\_Sys\_StirRandom |
| Tss2\_Sys\_HashSequenceStart\_Prepare | Tss2\_Sys\_HashSequenceStart\_Complete | Tss2\_Sys\_HashSequenceStart |
| Tss2\_Sys\_SequenceUpdate\_Prepare | Tss2\_Sys\_SequenceUpdate\_Complete | Tss2\_Sys\_SequenceUpdate |
| Tss2\_Sys\_SequenceComplete\_Prepare | Tss2\_Sys\_SequenceComplete\_Complete | Tss2\_Sys\_SequenceComplete |
| Tss2\_Sys\_Certify\_Prepare | Tss2\_Sys\_Certify\_Complete | Tss2\_Sys\_Certify |
| Tss2\_Sys\_CertifyCreation\_Prepare | Tss2\_Sys\_CertifyCreation\_Complete | Tss2\_Sys\_CertifyCreation |
| Tss2\_Sys\_Quote\_Prepare | Tss2\_Sys\_Quote\_Complete | Tss2\_Sys\_Quote |
| Tss2\_Sys\_Commit\_Prepare | Tss2\_Sys\_Commit\_Complete | Tss2\_Sys\_Commit |
| Tss2\_Sys\_EC\_Ephemeral\_Prepare | Tss2\_Sys\_EC\_Ephemeral\_Complete | Tss2\_Sys\_EC\_Ephemeral |
| Tss2\_Sys\_VerifySignature\_Prepare | Tss2\_Sys\_VerifySignature\_Complete | Tss2\_Sys\_VerifySignature |
| Tss2\_Sys\_Sign\_Prepare | Tss2\_Sys\_Sign\_Complete | Tss2\_Sys\_Sign |
| Tss2\_Sys\_PCR\_Extend\_Prepare | Tss2\_Sys\_PCR\_Extend\_Complete | Tss2\_Sys\_PCR\_Extend |
| Tss2\_Sys\_PCR\_Event\_Prepare | Tss2\_Sys\_PCR\_Event\_Complete | Tss2\_Sys\_PCR\_Event |
| Tss2\_Sys\_PCR\_Read\_Prepare | Tss2\_Sys\_PCR\_Read\_Complete | Tss2\_Sys\_PCR\_Read |
| Tss2\_Sys\_PCR\_Allocate\_Prepare | Tss2\_Sys\_PCR\_Allocate\_Complete | Tss2\_Sys\_PCR\_Allocate |
| Tss2\_Sys\_PCR\_Reset\_Prepare | Tss2\_Sys\_PCR\_Reset\_Complete | Tss2\_Sys\_PCR\_Reset |
| Tss2\_Sys\_PolicySigned\_Prepare | Tss2\_Sys\_PolicySigned\_Complete | Tss2\_Sys\_PolicySigned |
| Tss2\_Sys\_PolicySecret\_Prepare | Tss2\_Sys\_PolicySecret\_Complete | Tss2\_Sys\_PolicySecret |
| Tss2\_Sys\_PolicyTicket\_Prepare | Tss2\_Sys\_PolicyTicket\_Complete | Tss2\_Sys\_PolicyTicket |
| Tss2\_Sys\_PolicyOR\_Prepare | Tss2\_Sys\_PolicyOR\_Complete | Tss2\_Sys\_PolicyOR |
| Tss2\_Sys\_PolicyPCR\_Prepare | Tss2\_Sys\_PolicyPCR\_Complete | Tss2\_Sys\_PolicyPCR |
| Tss2\_Sys\_PolicyCommandCode\_Prepare | Tss2\_Sys\_PolicyCommandCode\_Complete | Tss2\_Sys\_PolicyCommandCode |
| Tss2\_Sys\_PolicyCpHash\_Prepare | Tss2\_Sys\_PolicyCpHash\_Complete | Tss2\_Sys\_PolicyCpHash |
| Tss2\_Sys\_PolicyAuthValue\_Prepare | Tss2\_Sys\_PolicyAuthValue\_Complete | Tss2\_Sys\_PolicyAuthValue |
| Tss2\_Sys\_PolicyPassword\_Prepare | Tss2\_Sys\_PolicyPassword\_Complete | Tss2\_Sys\_PolicyPassword |
| Tss2\_Sys\_PolicyGetDigest\_Prepare | Tss2\_Sys\_PolicyGetDigest\_Complete | Tss2\_Sys\_PolicyGetDigest |
| Tss2\_Sys\_CreatePrimary\_Prepare | Tss2\_Sys\_CreatePrimary\_Complete | Tss2\_Sys\_CreatePrimary |
| Tss2\_Sys\_HierarchyControl\_Prepare | Tss2\_Sys\_HierarchyControl\_Complete | Tss2\_Sys\_HierarchyControl |
| Tss2\_Sys\_Clear\_Prepare | Tss2\_Sys\_Clear\_Complete | Tss2\_Sys\_Clear |
| Tss2\_Sys\_ClearControl\_Prepare | Tss2\_Sys\_ClearControl\_Complete | Tss2\_Sys\_ClearControl |
| Tss2\_Sys\_HierarchyChangeAuth\_Prepare | Tss2\_Sys\_HierarchyChangeAuth\_Complete | Tss2\_Sys\_HierarchyChangeAuth |
| Tss2\_Sys\_DictionaryAttackLockReset\_Prepare | Tss2\_Sys\_DictionaryAttackLockReset\_Complete | Tss2\_Sys\_DictionaryAttackLockReset |
| Tss2\_Sys\_DictionaryAttackParameters\_Prepare | Tss2\_Sys\_DictionaryAttackParameters\_Complete | Tss2\_Sys\_DictionaryAttackParameters |
| Tss2\_Sys\_ContextSave\_Prepare | Tss2\_Sys\_ContextSave\_Complete | Tss2\_Sys\_ContextSave |
| Tss2\_Sys\_ContextLoad\_Prepare | Tss2\_Sys\_ContextLoad\_Complete | Tss2\_Sys\_ContextLoad |
| Tss2\_Sys\_FlushContext\_Prepare | Tss2\_Sys\_FlushContext\_Complete | Tss2\_Sys\_FlushContext |
| Tss2\_Sys\_EvictControl\_Prepare | Tss2\_Sys\_EvictControl\_Complete | Tss2\_Sys\_EvictControl |
| Tss2\_Sys\_GetCapability\_Prepare | Tss2\_Sys\_GetCapability\_Complete | Tss2\_Sys\_GetCapability |
| Tss2\_Sys\_TestParms\_Prepare | Tss2\_Sys\_TestParms\_Complete | Tss2\_Sys\_TestParms |
| Tss2\_Sys\_NV\_DefineSpace\_Prepare | Tss2\_Sys\_NV\_DefineSpace\_Complete | Tss2\_Sys\_NV\_DefineSpace |
| Tss2\_Sys\_NV\_UndefineSpace\_Prepare | Tss2\_Sys\_NV\_UndefineSpace\_Complete | Tss2\_Sys\_NV\_UndefineSpace |
| Tss2\_Sys\_NV\_ReadPublic\_Prepare | Tss2\_Sys\_NV\_ReadPublic\_Complete | Tss2\_Sys\_NV\_ReadPublic |
| Tss2\_Sys\_NV\_Write\_Prepare | Tss2\_Sys\_NV\_Write\_Complete | Tss2\_Sys\_NV\_Write |
| Tss2\_Sys\_NV\_Increment\_Prepare | Tss2\_Sys\_NV\_Increment\_Complete | Tss2\_Sys\_NV\_Increment |
| Tss2\_Sys\_NV\_Extend\_Prepare | Tss2\_Sys\_NV\_Extend\_Complete | Tss2\_Sys\_NV\_Extend |
| Tss2\_Sys\_NV\_SetBits\_Prepare | Tss2\_Sys\_NV\_SetBits\_Complete | Tss2\_Sys\_NV\_SetBits |
| Tss2\_Sys\_NV\_WriteLock\_Prepare | Tss2\_Sys\_NV\_WriteLock\_Complete | Tss2\_Sys\_NV\_WriteLock |
| Tss2\_Sys\_NV\_GlobalWriteLock\_Prepare | Tss2\_Sys\_NV\_GlobalWriteLock\_Complete | Tss2\_Sys\_NV\_GlobalWriteLock |
| Tss2\_Sys\_NV\_Read\_Prepare | Tss2\_Sys\_NV\_Read\_Complete | Tss2\_Sys\_NV\_Read |
| Tss2\_Sys\_NV\_ReadLock\_Prepare | Tss2\_Sys\_NV\_ReadLock\_Complete | Tss2\_Sys\_NV\_ReadLock |
| Tss2\_Sys\_NV\_ChangeAuth\_Prepare | Tss2\_Sys\_NV\_ChangeAuth\_Complete | Tss2\_Sys\_NV\_ChangeAuth |

## HiTSS支持的序列化和反序列化接口列表

| Marshal接口 | Unmarshal接口 |
| --- | --- |
| Tss2\_MU\_INT8\_Marshal | Tss2\_MU\_INT8\_Unmarshal |
| Tss2\_MU\_UINT8\_Marshal | Tss2\_MU\_UINT8\_Unmarshal |
| Tss2\_MU\_INT16\_Marshal | Tss2\_MU\_INT16\_Unmarshal |
| Tss2\_MU\_UINT16\_Marshal | Tss2\_MU\_UINT16\_Unmarshal |
| Tss2\_MU\_INT32\_Marshal | Tss2\_MU\_INT32\_Unmarshal |
| Tss2\_MU\_UINT32\_Marshal | Tss2\_MU\_UINT32\_Unmarshal |
| Tss2\_MU\_INT64\_Marshal | Tss2\_MU\_INT64\_Unmarshal |
| Tss2\_MU\_UINT64\_Marshal | Tss2\_MU\_UINT64\_Unmarshal |
| Tss2\_MU\_BYTE\_Marshal | Tss2\_MU\_BYTE\_Unmarshal |
| Tss2\_MU\_TPM2\_ALGORITHM\_ID\_Marshal | Tss2\_MU\_TPM2\_ALGORITHM\_ID\_Unmarshal |
| Tss2\_MU\_TPM2\_MODIFIER\_INDICATOR\_Marshal | Tss2\_MU\_TPM2\_MODIFIER\_INDICATOR\_Unmarshal |
| Tss2\_MU\_TPM2\_AUTHORIZATION\_SIZE\_Marshal | Tss2\_MU\_TPM2\_AUTHORIZATION\_SIZE\_Unmarshal |
| Tss2\_MU\_TPM2\_PARAMETER\_SIZE\_Marshal | Tss2\_MU\_TPM2\_PARAMETER\_SIZE\_Unmarshal |
| Tss2\_MU\_TPM2\_KEY\_SIZE\_Marshal | Tss2\_MU\_TPM2\_KEY\_SIZE\_Unmarshal |
| Tss2\_MU\_TPM2\_KEY\_BITS\_Marshal | Tss2\_MU\_TPM2\_KEY\_BITS\_Unmarshal |
| Tss2\_MU\_TPM2\_SPEC\_Marshal | Tss2\_MU\_TPM2\_SPEC\_Unmarshal |
| Tss2\_MU\_TPM2\_GENERATED\_Marshal | Tss2\_MU\_TPM2\_GENERATED\_Unmarshal |
| Tss2\_MU\_TPM2\_ALG\_ID\_Marshal | Tss2\_MU\_TPM2\_ALG\_ID\_Unmarshal |
| Tss2\_MU\_TPM2\_ECC\_CURVE\_Marshal | Tss2\_MU\_TPM2\_ECC\_CURVE\_Unmarshal |
| Tss2\_MU\_TPM2\_CC\_Marshal | Tss2\_MU\_TPM2\_CC\_Unmarshal |
| Tss2\_MU\_TPM2\_RC\_Marshal | Tss2\_MU\_TPM2\_RC\_Unmarshal |
| Tss2\_MU\_TPM2\_CLOCK\_ADJUST\_Marshal | Tss2\_MU\_TPM2\_CLOCK\_ADJUST\_Unmarshal |
| Tss2\_MU\_TPM2\_EO\_Marshal | Tss2\_MU\_TPM2\_EO\_Unmarshal |
| Tss2\_MU\_TPM2\_ST\_Marshal | Tss2\_MU\_TPM2\_ST\_Unmarshal |
| Tss2\_MU\_TPM2\_SU\_Marshal | Tss2\_MU\_TPM2\_SU\_Unmarshal |
| Tss2\_MU\_TPM2\_SE\_Marshal | Tss2\_MU\_TPM2\_SE\_Unmarshal |
| Tss2\_MU\_TPM2\_CAP\_Marshal | Tss2\_MU\_TPM2\_CAP\_Unmarshal |
| Tss2\_MU\_TPM2\_PT\_Marshal | Tss2\_MU\_TPM2\_PT\_Unmarshal |
| Tss2\_MU\_TPM2\_PT\_PCR\_Marshal | Tss2\_MU\_TPM2\_PT\_PCR\_Unmarshal |
| Tss2\_MU\_TPM2\_PS\_Marshal | Tss2\_MU\_TPM2\_PS\_Unmarshal |
| Tss2\_MU\_TPM2\_HANDLE\_Marshal | Tss2\_MU\_TPM2\_HANDLE\_Unmarshal |
| Tss2\_MU\_TPM2\_HT\_Marshal | Tss2\_MU\_TPM2\_HT\_Unmarshal |
| Tss2\_MU\_TPM2\_RH\_Marshal | Tss2\_MU\_TPM2\_RH\_Unmarshal |
| Tss2\_MU\_TPM2\_HC\_Marshal | Tss2\_MU\_TPM2\_HC\_Unmarshal |
| Tss2\_MU\_TPMA\_ALGORITHM\_Marshal | Tss2\_MU\_TPMA\_ALGORITHM\_Unmarshal |
| Tss2\_MU\_TPMA\_OBJECT\_Marshal | Tss2\_MU\_TPMA\_OBJECT\_Unmarshal |
| Tss2\_MU\_TPMA\_SESSION\_Marshal | Tss2\_MU\_TPMA\_SESSION\_Unmarshal |
| Tss2\_MU\_TPMA\_LOCALITY\_Marshal | Tss2\_MU\_TPMA\_LOCALITY\_Unmarshal |
| Tss2\_MU\_TPMA\_PERMANENT\_Marshal | Tss2\_MU\_TPMA\_PERMANENT\_Unmarshal |
| Tss2\_MU\_TPMA\_STARTUP\_CLEAR\_Marshal | Tss2\_MU\_TPMA\_STARTUP\_CLEAR\_Unmarshal |
| Tss2\_MU\_TPMA\_MEMORY\_Marshal | Tss2\_MU\_TPMA\_MEMORY\_Unmarshal |
| Tss2\_MU\_TPMA\_CC\_Marshal | Tss2\_MU\_TPMA\_CC\_Unmarshal |
| Tss2\_MU\_TPMA\_MODES\_Marshal | Tss2\_MU\_TPMA\_MODES\_Unmarshal |
| Tss2\_MU\_TPMA\_X509\_KEY\_USAGE\_Marshal | Tss2\_MU\_TPMA\_X509\_KEY\_USAGE\_Unmarshal |
| Tss2\_MU\_TPMI\_YES\_NO\_Marshal | Tss2\_MU\_TPMI\_YES\_NO\_Unmarshal |
| Tss2\_MU\_TPMI\_DH\_OBJECT\_Marshal | Tss2\_MU\_TPMI\_DH\_OBJECT\_Unmarshal |
| Tss2\_MU\_TPMI\_DH\_PARENT\_Marshal | Tss2\_MU\_TPMI\_DH\_PARENT\_Unmarshal |
| Tss2\_MU\_TPMI\_DH\_PERSISTENT\_Marshal | Tss2\_MU\_TPMI\_DH\_PERSISTENT\_Unmarshal |
| Tss2\_MU\_TPMI\_DH\_ENTITY\_Marshal | Tss2\_MU\_TPMI\_DH\_ENTITY\_Unmarshal |
| Tss2\_MU\_TPMI\_DH\_PCR\_Marshal | Tss2\_MU\_TPMI\_DH\_PCR\_Unmarshal |
| Tss2\_MU\_TPMI\_SH\_AUTH\_SESSION\_Marshal | Tss2\_MU\_TPMI\_SH\_AUTH\_SESSION\_Unmarshal |
| Tss2\_MU\_TPMI\_SH\_HMAC\_Marshal | Tss2\_MU\_TPMI\_SH\_HMAC\_Unmarshal |
| Tss2\_MU\_TPMI\_SH\_POLICY\_Marshal | Tss2\_MU\_TPMI\_SH\_POLICY\_Unmarshal |
| Tss2\_MU\_TPMI\_DH\_CONTEXT\_Marshal | Tss2\_MU\_TPMI\_DH\_CONTEXT\_Unmarshal |
| Tss2\_MU\_TPMI\_DH\_SAVED\_Marshal | Tss2\_MU\_TPMI\_DH\_SAVED\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_HIERARCHY\_Marshal | Tss2\_MU\_TPMI\_RH\_HIERARCHY\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_ENABLES\_Marshal | Tss2\_MU\_TPMI\_RH\_ENABLES\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_HIERARCHY\_AUTH\_Marshal | Tss2\_MU\_TPMI\_RH\_HIERARCHY\_AUTH\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_HIERARCHY\_POLICY\_Marshal | Tss2\_MU\_TPMI\_RH\_HIERARCHY\_POLICY\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_PLATFORM\_Marshal | Tss2\_MU\_TPMI\_RH\_PLATFORM\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_OWNER\_Marshal | Tss2\_MU\_TPMI\_RH\_OWNER\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_ENDORSEMENT\_Marshal | Tss2\_MU\_TPMI\_RH\_ENDORSEMENT\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_PROVISION\_Marshal | Tss2\_MU\_TPMI\_RH\_PROVISION\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_CLEAR\_Marshal | Tss2\_MU\_TPMI\_RH\_CLEAR\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_NV\_AUTH\_Marshal | Tss2\_MU\_TPMI\_RH\_NV\_AUTH\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_LOCKOUT\_Marshal | Tss2\_MU\_TPMI\_RH\_LOCKOUT\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_NV\_INDEX\_Marshal | Tss2\_MU\_TPMI\_RH\_NV\_INDEX\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_AC\_Marshal | Tss2\_MU\_TPMI\_RH\_AC\_Unmarshal |
| Tss2\_MU\_TPMI\_RH\_ACT\_Marshal | Tss2\_MU\_TPMI\_RH\_ACT\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_HASH\_Marshal | Tss2\_MU\_TPMI\_ALG\_HASH\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_ASYM\_Marshal | Tss2\_MU\_TPMI\_ALG\_ASYM\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_SYM\_Marshal | Tss2\_MU\_TPMI\_ALG\_SYM\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_SYM\_OBJECT\_Marshal | Tss2\_MU\_TPMI\_ALG\_SYM\_OBJECT\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_SYM\_MODE\_Marshal | Tss2\_MU\_TPMI\_ALG\_SYM\_MODE\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_KDF\_Marshal | Tss2\_MU\_TPMI\_ALG\_KDF\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_SIG\_SCHEME\_Marshal | Tss2\_MU\_TPMI\_ALG\_SIG\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMI\_ECC\_KEY\_EXCHANGE\_Marshal | Tss2\_MU\_TPMI\_ECC\_KEY\_EXCHANGE\_Unmarshal |
| Tss2\_MU\_TPMI\_ST\_COMMAND\_TAG\_Marshal | Tss2\_MU\_TPMI\_ST\_COMMAND\_TAG\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_MAC\_SCHEME\_Marshal | Tss2\_MU\_TPMI\_ALG\_MAC\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_CIPHER\_MODE\_Marshal | Tss2\_MU\_TPMI\_ALG\_CIPHER\_MODE\_Unmarshal |
| Tss2\_MU\_TPMS\_EMPTY\_Marshal | Tss2\_MU\_TPMS\_EMPTY\_Unmarshal |
| Tss2\_MU\_TPMS\_ALGORITHM\_DESCRIPTION\_Marshal | Tss2\_MU\_TPMS\_ALGORITHM\_DESCRIPTION\_Unmarshal |
| Tss2\_MU\_TPMU\_HA\_Marshal | Tss2\_MU\_TPMU\_HA\_Unmarshal |
| Tss2\_MU\_TPMT\_HA\_Marshal | Tss2\_MU\_TPMT\_HA\_Unmarshal |
| Tss2\_MU\_TPM2B\_DIGEST\_Marshal | Tss2\_MU\_TPM2B\_DIGEST\_Unmarshal |
| Tss2\_MU\_TPM2B\_DATA\_Marshal | Tss2\_MU\_TPM2B\_DATA\_Unmarshal |
| Tss2\_MU\_TPM2B\_NONCE\_Marshal | Tss2\_MU\_TPM2B\_NONCE\_Unmarshal |
| Tss2\_MU\_TPM2B\_AUTH\_Marshal | Tss2\_MU\_TPM2B\_AUTH\_Unmarshal |
| Tss2\_MU\_TPM2B\_OPERAND\_Marshal | Tss2\_MU\_TPM2B\_OPERAND\_Unmarshal |
| Tss2\_MU\_TPM2B\_EVENT\_Marshal | Tss2\_MU\_TPM2B\_EVENT\_Unmarshal |
| Tss2\_MU\_TPM2B\_MAX\_BUFFER\_Marshal | Tss2\_MU\_TPM2B\_MAX\_BUFFER\_Unmarshal |
| Tss2\_MU\_TPM2B\_MAX\_NV\_BUFFER\_Marshal | Tss2\_MU\_TPM2B\_MAX\_NV\_BUFFER\_Unmarshal |
| Tss2\_MU\_TPM2B\_TIMEOUT\_Marshal | Tss2\_MU\_TPM2B\_TIMEOUT\_Unmarshal |
| Tss2\_MU\_TPM2B\_IV\_Marshal | Tss2\_MU\_TPM2B\_IV\_Unmarshal |
| Tss2\_MU\_TPMU\_NAME\_Marshal | Tss2\_MU\_TPMU\_NAME\_Unmarshal |
| Tss2\_MU\_TPM2B\_NAME\_Marshal | Tss2\_MU\_TPM2B\_NAME\_Unmarshal |
| Tss2\_MU\_TPMS\_PCR\_SELECT\_Marshal | Tss2\_MU\_TPMS\_PCR\_SELECT\_Unmarshal |
| Tss2\_MU\_TPMS\_PCR\_SELECTION\_Marshal | Tss2\_MU\_TPMS\_PCR\_SELECTION\_Unmarshal |
| Tss2\_MU\_TPMT\_TK\_CREATION\_Marshal | Tss2\_MU\_TPMT\_TK\_CREATION\_Unmarshal |
| Tss2\_MU\_TPMT\_TK\_VERIFIED\_Marshal | Tss2\_MU\_TPMT\_TK\_VERIFIED\_Unmarshal |
| Tss2\_MU\_TPMT\_TK\_AUTH\_Marshal | Tss2\_MU\_TPMT\_TK\_AUTH\_Unmarshal |
| Tss2\_MU\_TPMT\_TK\_HASHCHECK\_Marshal | Tss2\_MU\_TPMT\_TK\_HASHCHECK\_Unmarshal |
| Tss2\_MU\_TPMS\_ALG\_PROPERTY\_Marshal | Tss2\_MU\_TPMS\_ALG\_PROPERTY\_Unmarshal |
| Tss2\_MU\_TPMS\_TAGGED\_PROPERTY\_Marshal | Tss2\_MU\_TPMS\_TAGGED\_PROPERTY\_Unmarshal |
| Tss2\_MU\_TPMS\_TAGGED\_PCR\_SELECT\_Marshal | Tss2\_MU\_TPMS\_TAGGED\_PCR\_SELECT\_Unmarshal |
| Tss2\_MU\_TPMS\_TAGGED\_POLICY\_Marshal | Tss2\_MU\_TPMS\_TAGGED\_POLICY\_Unmarshal |
| Tss2\_MU\_TPML\_CC\_Marshal | Tss2\_MU\_TPML\_CC\_Unmarshal |
| Tss2\_MU\_TPML\_CCA\_Marshal | Tss2\_MU\_TPML\_CCA\_Unmarshal |
| Tss2\_MU\_TPML\_ALG\_Marshal | Tss2\_MU\_TPML\_ALG\_Unmarshal |
| Tss2\_MU\_TPML\_HANDLE\_Marshal | Tss2\_MU\_TPML\_HANDLE\_Unmarshal |
| Tss2\_MU\_TPML\_DIGEST\_Marshal | Tss2\_MU\_TPML\_DIGEST\_Unmarshal |
| Tss2\_MU\_TPML\_DIGEST\_VALUES\_Marshal | Tss2\_MU\_TPML\_DIGEST\_VALUES\_Unmarshal |
| Tss2\_MU\_TPML\_PCR\_SELECTION\_Marshal | Tss2\_MU\_TPML\_PCR\_SELECTION\_Unmarshal |
| Tss2\_MU\_TPML\_ALG\_PROPERTY\_Marshal | Tss2\_MU\_TPML\_ALG\_PROPERTY\_Unmarshal |
| Tss2\_MU\_TPML\_TAGGED\_TPM\_PROPERTY\_Marshal | Tss2\_MU\_TPML\_TAGGED\_TPM\_PROPERTY\_Unmarshal |
| Tss2\_MU\_TPML\_TAGGED\_PCR\_PROPERTY\_Marshal | Tss2\_MU\_TPML\_TAGGED\_PCR\_PROPERTY\_Unmarshal |
| Tss2\_MU\_TPML\_ECC\_CURVE\_Marshal | Tss2\_MU\_TPML\_ECC\_CURVE\_Unmarshal |
| Tss2\_MU\_TPML\_TAGGED\_POLICY\_Marshal | Tss2\_MU\_TPML\_TAGGED\_POLICY\_Unmarshal |
| Tss2\_MU\_TPMU\_CAPABILITIES\_Marshal | Tss2\_MU\_TPMU\_CAPABILITIES\_Unmarshal |
| Tss2\_MU\_TPMS\_CAPABILITY\_DATA\_Marshal | Tss2\_MU\_TPMS\_CAPABILITY\_DATA\_Unmarshal |
| Tss2\_MU\_TPMS\_CLOCK\_INFO\_Marshal | Tss2\_MU\_TPMS\_CLOCK\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_TIME\_INFO\_Marshal | Tss2\_MU\_TPMS\_TIME\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_TIME\_ATTEST\_INFO\_Marshal | Tss2\_MU\_TPMS\_TIME\_ATTEST\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_CERTIFY\_INFO\_Marshal | Tss2\_MU\_TPMS\_CERTIFY\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_QUOTE\_INFO\_Marshal | Tss2\_MU\_TPMS\_QUOTE\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_COMMAND\_AUDIT\_INFO\_Marshal | Tss2\_MU\_TPMS\_COMMAND\_AUDIT\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_SESSION\_AUDIT\_INFO\_Marshal | Tss2\_MU\_TPMS\_SESSION\_AUDIT\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_CREATION\_INFO\_Marshal | Tss2\_MU\_TPMS\_CREATION\_INFO\_Unmarshal |
| Tss2\_MU\_TPMS\_NV\_CERTIFY\_INFO\_Marshal | Tss2\_MU\_TPMS\_NV\_CERTIFY\_INFO\_Unmarshal |
| Tss2\_MU\_TPMI\_ST\_ATTEST\_Marshal | Tss2\_MU\_TPMI\_ST\_ATTEST\_Unmarshal |
| Tss2\_MU\_TPMU\_ATTEST\_Marshal | Tss2\_MU\_TPMU\_ATTEST\_Unmarshal |
| Tss2\_MU\_TPMS\_ATTEST\_Marshal | Tss2\_MU\_TPMS\_ATTEST\_Unmarshal |
| Tss2\_MU\_TPM2B\_ATTEST\_Marshal | Tss2\_MU\_TPM2B\_ATTEST\_Unmarshal |
| Tss2\_MU\_TPMS\_AUTH\_COMMAND\_Marshal | Tss2\_MU\_TPMS\_AUTH\_COMMAND\_Unmarshal |
| Tss2\_MU\_TPMS\_AUTH\_RESPONSE\_Marshal | Tss2\_MU\_TPMS\_AUTH\_RESPONSE\_Unmarshal |
| Tss2\_MU\_TPMI\_AES\_KEY\_BITS\_Marshal | Tss2\_MU\_TPMI\_AES\_KEY\_BITS\_Unmarshal |
| Tss2\_MU\_TPMI\_SM4\_KEY\_BITS\_Marshal | Tss2\_MU\_TPMI\_SM4\_KEY\_BITS\_Unmarshal |
| Tss2\_MU\_TPMI\_CAMELLIA\_KEY\_BITS\_Marshal | Tss2\_MU\_TPMI\_CAMELLIA\_KEY\_BITS\_Unmarshal |
| Tss2\_MU\_TPMU\_SYM\_KEY\_BITS\_Marshal | Tss2\_MU\_TPMU\_SYM\_KEY\_BITS\_Unmarshal |
| Tss2\_MU\_TPMU\_SYM\_MODE\_Marshal | Tss2\_MU\_TPMU\_SYM\_MODE\_Unmarshal |
| Tss2\_MU\_TPMT\_SYM\_DEF\_Marshal | Tss2\_MU\_TPMT\_SYM\_DEF\_Unmarshal |
| Tss2\_MU\_TPMT\_SYM\_DEF\_OBJECT\_Marshal | Tss2\_MU\_TPMT\_SYM\_DEF\_OBJECT\_Unmarshal |
| Tss2\_MU\_TPM2B\_SYM\_KEY\_Marshal | Tss2\_MU\_TPM2B\_SYM\_KEY\_Unmarshal |
| Tss2\_MU\_TPMS\_SYMCIPHER\_PARMS\_Marshal | Tss2\_MU\_TPMS\_SYMCIPHER\_PARMS\_Unmarshal |
| Tss2\_MU\_TPM2B\_LABEL\_Marshal | Tss2\_MU\_TPM2B\_LABEL\_Unmarshal |
| Tss2\_MU\_TPMS\_DERIVE\_Marshal | Tss2\_MU\_TPMS\_DERIVE\_Unmarshal |
| Tss2\_MU\_TPM2B\_DERIVE\_Marshal | Tss2\_MU\_TPM2B\_DERIVE\_Unmarshal |
| Tss2\_MU\_TPMU\_SENSITIVE\_CREATE\_Marshal | Tss2\_MU\_TPMU\_SENSITIVE\_CREATE\_Unmarshal |
| Tss2\_MU\_TPM2B\_SENSITIVE\_DATA\_Marshal | Tss2\_MU\_TPM2B\_SENSITIVE\_DATA\_Unmarshal |
| Tss2\_MU\_TPMS\_SENSITIVE\_CREATE\_Marshal | Tss2\_MU\_TPMS\_SENSITIVE\_CREATE\_Unmarshal |
| Tss2\_MU\_TPM2B\_SENSITIVE\_CREATE\_Marshal | Tss2\_MU\_TPM2B\_SENSITIVE\_CREATE\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_HASH\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_HASH\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_ECDAA\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_ECDAA\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_KEYEDHASH\_SCHEME\_Marshal | Tss2\_MU\_TPMI\_ALG\_KEYEDHASH\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_HMAC\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_HMAC\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_XOR\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_XOR\_Unmarshal |
| Tss2\_MU\_TPMU\_SCHEME\_KEYEDHASH\_Marshal | Tss2\_MU\_TPMU\_SCHEME\_KEYEDHASH\_Unmarshal |
| Tss2\_MU\_TPMT\_KEYEDHASH\_SCHEME\_Marshal | Tss2\_MU\_TPMT\_KEYEDHASH\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSASSA\_Marshal | Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSASSA\_Unmarshal |
| Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSAPSS\_Marshal | Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSAPSS\_Unmarshal |
| Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDSA\_Marshal | Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDSA\_Unmarshal |
| Tss2\_MU\_TPMS\_SIG\_SCHEME\_SM2\_Marshal | Tss2\_MU\_TPMS\_SIG\_SCHEME\_SM2\_Unmarshal |
| Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECSCHNORR\_Marshal | Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECSCHNORR\_Unmarshal |
| Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDAA\_Marshal | Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDAA\_Unmarshal |
| Tss2\_MU\_TPMU\_SIG\_SCHEME\_Marshal | Tss2\_MU\_TPMU\_SIG\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMT\_SIG\_SCHEME\_Marshal | Tss2\_MU\_TPMT\_SIG\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMS\_ENC\_SCHEME\_OAEP\_Marshal | Tss2\_MU\_TPMS\_ENC\_SCHEME\_OAEP\_Unmarshal |
| Tss2\_MU\_TPMS\_ENC\_SCHEME\_RSAES\_Marshal | Tss2\_MU\_TPMS\_ENC\_SCHEME\_RSAES\_Unmarshal |
| Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECDH\_Marshal | Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECDH\_Unmarshal |
| Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECMQV\_Marshal | Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECMQV\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_MGF1\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_MGF1\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_56A\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_56A\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_KDF2\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_KDF2\_Unmarshal |
| Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_108\_Marshal | Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_108\_Unmarshal |
| Tss2\_MU\_TPMU\_KDF\_SCHEME\_Marshal | Tss2\_MU\_TPMU\_KDF\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMT\_KDF\_SCHEME\_Marshal | Tss2\_MU\_TPMT\_KDF\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_ASYM\_SCHEME\_Marshal | Tss2\_MU\_TPMI\_ALG\_ASYM\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMU\_ASYM\_SCHEME\_Marshal | Tss2\_MU\_TPMU\_ASYM\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMT\_ASYM\_SCHEME\_Marshal | Tss2\_MU\_TPMT\_ASYM\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_RSA\_SCHEME\_Marshal | Tss2\_MU\_TPMI\_ALG\_RSA\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMT\_RSA\_SCHEME\_Marshal | Tss2\_MU\_TPMT\_RSA\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_RSA\_DECRYPT\_Marshal | Tss2\_MU\_TPMI\_ALG\_RSA\_DECRYPT\_Unmarshal |
| Tss2\_MU\_TPMT\_RSA\_DECRYPT\_Marshal | Tss2\_MU\_TPMT\_RSA\_DECRYPT\_Unmarshal |
| Tss2\_MU\_TPM2B\_PUBLIC\_KEY\_RSA\_Marshal | Tss2\_MU\_TPM2B\_PUBLIC\_KEY\_RSA\_Unmarshal |
| Tss2\_MU\_TPMI\_RSA\_KEY\_BITS\_Marshal | Tss2\_MU\_TPMI\_RSA\_KEY\_BITS\_Unmarshal |
| Tss2\_MU\_TPM2B\_PRIVATE\_KEY\_RSA\_Marshal | Tss2\_MU\_TPM2B\_PRIVATE\_KEY\_RSA\_Unmarshal |
| Tss2\_MU\_TPM2B\_ECC\_PARAMETER\_Marshal | Tss2\_MU\_TPM2B\_ECC\_PARAMETER\_Unmarshal |
| Tss2\_MU\_TPMS\_ECC\_POINT\_Marshal | Tss2\_MU\_TPMS\_ECC\_POINT\_Unmarshal |
| Tss2\_MU\_TPM2B\_ECC\_POINT\_Marshal | Tss2\_MU\_TPM2B\_ECC\_POINT\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_ECC\_SCHEME\_Marshal | Tss2\_MU\_TPMI\_ALG\_ECC\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMI\_ECC\_CURVE\_Marshal | Tss2\_MU\_TPMI\_ECC\_CURVE\_Unmarshal |
| Tss2\_MU\_TPMT\_ECC\_SCHEME\_Marshal | Tss2\_MU\_TPMT\_ECC\_SCHEME\_Unmarshal |
| Tss2\_MU\_TPMS\_ALGORITHM\_DETAIL\_ECC\_Marshal | Tss2\_MU\_TPMS\_ALGORITHM\_DETAIL\_ECC\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_RSA\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_RSA\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_RSASSA\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_RSASSA\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_RSAPSS\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_RSAPSS\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_ECC\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_ECC\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_ECDSA\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_ECDSA\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_ECDAA\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_ECDAA\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_SM2\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_SM2\_Unmarshal |
| Tss2\_MU\_TPMS\_SIGNATURE\_ECSCHNORR\_Marshal | Tss2\_MU\_TPMS\_SIGNATURE\_ECSCHNORR\_Unmarshal |
| Tss2\_MU\_TPMU\_SIGNATURE\_Marshal | Tss2\_MU\_TPMU\_SIGNATURE\_Unmarshal |
| Tss2\_MU\_TPMT\_SIGNATURE\_Marshal | Tss2\_MU\_TPMT\_SIGNATURE\_Unmarshal |
| Tss2\_MU\_TPMU\_ENCRYPTED\_SECRET\_Marshal | Tss2\_MU\_TPMU\_ENCRYPTED\_SECRET\_Unmarshal |
| Tss2\_MU\_TPM2B\_ENCRYPTED\_SECRET\_Marshal | Tss2\_MU\_TPM2B\_ENCRYPTED\_SECRET\_Unmarshal |
| Tss2\_MU\_TPMI\_ALG\_PUBLIC\_Marshal | Tss2\_MU\_TPMI\_ALG\_PUBLIC\_Unmarshal |
| Tss2\_MU\_TPMU\_PUBLIC\_ID\_Marshal | Tss2\_MU\_TPMU\_PUBLIC\_ID\_Unmarshal |
| Tss2\_MU\_TPMS\_KEYEDHASH\_PARMS\_Marshal | Tss2\_MU\_TPMS\_KEYEDHASH\_PARMS\_Unmarshal |
| Tss2\_MU\_TPMS\_ASYM\_PARMS\_Marshal | Tss2\_MU\_TPMS\_ASYM\_PARMS\_Unmarshal |
| Tss2\_MU\_TPMS\_RSA\_PARMS\_Marshal | Tss2\_MU\_TPMS\_RSA\_PARMS\_Unmarshal |
| Tss2\_MU\_TPMS\_ECC\_PARMS\_Marshal | Tss2\_MU\_TPMS\_ECC\_PARMS\_Unmarshal |
| Tss2\_MU\_TPMU\_PUBLIC\_PARMS\_Marshal | Tss2\_MU\_TPMU\_PUBLIC\_PARMS\_Unmarshal |
| Tss2\_MU\_TPMT\_PUBLIC\_PARMS\_Marshal | Tss2\_MU\_TPMT\_PUBLIC\_PARMS\_Unmarshal |
| Tss2\_MU\_TPMT\_PUBLIC\_Marshal | Tss2\_MU\_TPMT\_PUBLIC\_Unmarshal |
| Tss2\_MU\_TPM2B\_PUBLIC\_Marshal | Tss2\_MU\_TPM2B\_PUBLIC\_Unmarshal |
| Tss2\_MU\_TPM2B\_TEMPLATE\_Marshal | Tss2\_MU\_TPM2B\_TEMPLATE\_Unmarshal |
| Tss2\_MU\_TPM2B\_PRIVATE\_VENDOR\_SPECIFIC\_Marshal | Tss2\_MU\_TPM2B\_PRIVATE\_VENDOR\_SPECIFIC\_Unmarshal |
| Tss2\_MU\_TPMU\_SENSITIVE\_COMPOSITE\_Marshal | Tss2\_MU\_TPMU\_SENSITIVE\_COMPOSITE\_Unmarshal |
| Tss2\_MU\_TPMT\_SENSITIVE\_Marshal | Tss2\_MU\_TPMT\_SENSITIVE\_Unmarshal |
| Tss2\_MU\_TPM2B\_SENSITIVE\_Marshal | Tss2\_MU\_TPM2B\_SENSITIVE\_Unmarshal |
| Tss2\_MU\_\_PRIVATE\_Marshal | Tss2\_MU\_\_PRIVATE\_Unmarshal |
| Tss2\_MU\_TPM2B\_PRIVATE\_Marshal | Tss2\_MU\_TPM2B\_PRIVATE\_Unmarshal |
| Tss2\_MU\_TPMS\_ID\_OBJECT\_Marshal | Tss2\_MU\_TPMS\_ID\_OBJECT\_Unmarshal |
| Tss2\_MU\_TPM2B\_ID\_OBJECT\_Marshal | Tss2\_MU\_TPM2B\_ID\_OBJECT\_Unmarshal |
| Tss2\_MU\_TPM2\_NV\_INDEX\_Marshal | Tss2\_MU\_TPM2\_NV\_INDEX\_Unmarshal |
| Tss2\_MU\_TPM2\_NT\_Marshal | Tss2\_MU\_TPM2\_NT\_Unmarshal |
| Tss2\_MU\_TPMS\_NV\_PIN\_COUNTER\_PARAMETERS\_Marshal | Tss2\_MU\_TPMS\_NV\_PIN\_COUNTER\_PARAMETERS\_Unmarshal |
| Tss2\_MU\_TPMA\_NV\_Marshal | Tss2\_MU\_TPMA\_NV\_Unmarshal |
| Tss2\_MU\_TPMS\_NV\_PUBLIC\_Marshal | Tss2\_MU\_TPMS\_NV\_PUBLIC\_Unmarshal |
| Tss2\_MU\_TPM2B\_NV\_PUBLIC\_Marshal | Tss2\_MU\_TPM2B\_NV\_PUBLIC\_Unmarshal |
| Tss2\_MU\_TPM2B\_CONTEXT\_SENSITIVE\_Marshal | Tss2\_MU\_TPM2B\_CONTEXT\_SENSITIVE\_Unmarshal |
| Tss2\_MU\_TPMS\_CONTEXT\_DATA\_Marshal | Tss2\_MU\_TPMS\_CONTEXT\_DATA\_Unmarshal |
| Tss2\_MU\_TPM2B\_CONTEXT\_DATA\_Marshal | Tss2\_MU\_TPM2B\_CONTEXT\_DATA\_Unmarshal |
| Tss2\_MU\_TPMS\_CONTEXT\_Marshal | Tss2\_MU\_TPMS\_CONTEXT\_Unmarshal |
| Tss2\_MU\_TPMS\_CREATION\_DATA\_Marshal | Tss2\_MU\_TPMS\_CREATION\_DATA\_Unmarshal |
| Tss2\_MU\_TPM2B\_CREATION\_DATA\_Marshal | Tss2\_MU\_TPM2B\_CREATION\_DATA\_Unmarshal |
| Tss2\_MU\_TPMS\_ACT\_DATA\_Marshal | Tss2\_MU\_TPMS\_ACT\_DATA\_Unmarshal |
| Tss2\_MU\_TPMA\_ACT\_Marshal | Tss2\_MU\_TPMA\_ACT\_Unmarshal |
| Tss2\_MU\_TPM2\_AT\_Marshal | Tss2\_MU\_TPM2\_AT\_Unmarshal |
| Tss2\_MU\_TPMS\_NV\_DIGEST\_CERTIFY\_INFO\_Marshal | Tss2\_MU\_TPMS\_NV\_DIGEST\_CERTIFY\_INFO\_Unmarshal |
| Tss2\_MU\_TPMI\_TDES\_KEY\_BITS\_Marshal | Tss2\_MU\_TPMI\_TDES\_KEY\_BITS\_Unmarshal |
| Tss2\_MU\_TPMS\_AC\_OUTPUT\_Marshal | Tss2\_MU\_TPMS\_AC\_OUTPUT\_Unmarshal |
| Tss2\_MU\_TPML\_ACT\_DATA\_Marshal | Tss2\_MU\_TPML\_ACT\_DATA\_Unmarshal |
| Tss2\_MU\_TPML\_AC\_CAPABILITIES\_Marshal | Tss2\_MU\_TPML\_AC\_CAPABILITIES\_Unmarshal |

## HiTSS支持的命令传输接口列表

* Tss2\_TctiLdr\_Initialize
* Tss2\_TctiLdr\_Initialize\_Ex
* Tss2\_TctiLdr\_Finalize
* Tss2\_TctiLdr\_GetInfo
* Tss2\_TctiLdr\_FreeInfo

## 模拟器支持情况

本Kit暂不支持模拟器。

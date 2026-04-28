---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hapsigntool-errorcode
title: 签名工具错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > 签名工具错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:29+08:00
doc_updated_at: 2026-01-30
content_hash: sha256:50ee255bd9820506e73dee3bc995308f958b5d1c7c92ce10c4eadc727169c5a3
---

## 11010001 未知错误

**错误信息**

Unknown error.

**错误描述**

签名过程中出现系统内部错误。

**可能原因**

签名过程发生了错误，请查看日志中的签名验证失败详情。

**处理步骤**

结合控制台输出的错误日志信息及应用包进一步分析。

## 11012002 输入文件不存在

**错误信息**

File not exist.

**错误描述**

输入文件不存在。

**可能原因**

1. inFile参数指定的输入文件不存在。
2. appCertFile参数指定的证书文件不存在。
3. profileFile参数指定的profile文件不存在。

**处理步骤**

1. 检查inFile参数指定的输入文件是否存在。
2. 检查appCertFile参数指定的证书文件是否存在。
3. 检查profileFile参数指定的profile文件是否存在。

## 11012003 写文件错误

**错误信息**

Write file failed.

**错误描述**

写文件错误。

**可能原因**

当前用户没有outFile参数指定的输出文件的写权限。

**处理步骤**

检查当前用户是否有outFile参数指定的输出文件的写权限。

## 11012004 读文件错误

**错误信息**

Read file failed.

**错误描述**

读文件错误。

**可能原因**

profileFile参数指定的文件不存在，或当前用户没有该文件的读权限。

**处理步骤**

检查profileFile参数指定的文件是否存在，当前用户是否有该文件的读权限。

## 11012005 不支持的文件格式

**错误信息**

Not support file.

**错误描述**

不支持的文件格式。

**可能原因**

签名过程输入了不支持的文件后缀。

**处理步骤**

输入正确的文件格式。具体格式如下：

1. 已签名的profile文件后缀为p7b。
2. 未签名的profile文件后缀为json。
3. 证书或证书链文件后缀为cer。
4. 密钥库文件后缀为：jks、p12。

## 11012006 文件IO错误

**错误信息**

File IO failed.

**错误描述**

签名过程中发生文件读取或写入错误。

**可能原因**

1. inFile、keystoreFile、profileFile或appCertFile参数指定的文件不存在或当前用户没有读权限。
2. 当前用户没有outFile参数指定的输出文件的写权限。

**处理步骤**

1. 检查inFile、keystoreFile、profileFile或appCertFile参数指定的文件是否存在，且当前用户是否有读权限。
2. 检查当前用户是否有outFile参数指定的输出文件的写权限。

## 11013002 证书链文件错误

**错误信息**

Certificate format is incorrect, please check your appCertFile parameter.

**错误描述**

证书链文件错误。

**可能原因**

1. appCertFile参数指定的证书链文件内容不是X.509标准证书或文件内容被修改。
2. appCertFile参数指定的证书链文件内的证书已过期。

**处理步骤**

1. 检查appCertFile指定的文件内容是否标准X.509证书。
2. 更新证书链文件。

## 11014001 密钥不存在

**错误信息**

Key alias not found.

**错误描述**

密钥库中不存在指定别名的密钥。

**可能原因**

密钥库中不存在keyAlias参数指定的密钥。

**处理步骤**

检查密钥库是否存在keyAlias参数指定的密钥。

## 11014003 Keystore初始化失败

**错误信息**

Init keystore failed.

**错误描述**

Keystore初始化失败。

**可能原因**

1. 密钥库文件不存在。
2. 密钥库文件口令不正确。
3. 当前运行环境的JDK版本低于生成密钥库文件使用的JDK版本。

**处理步骤**

1. 检查密钥库文件是否存在。
2. 检查密钥库文件口令是否正确。
3. 检查当前运行环境的JDK版本。

## 11014007 密钥口令错误

**错误信息**

Key alias xxx password error.

**错误描述**

密钥口令错误。

**可能原因**

密钥口令错误。

**处理步骤**

检查keyAlias指定的密钥口令。

## 11014008 找不到可用证书

**错误信息**

No usable cert found in xxx.

**错误描述**

找不到可用证书。

**可能原因**

密钥库文件keyAlias指定的密钥条目对应的证书已过期。

**处理步骤**

检查密钥库文件keyAlias指定的密钥条目对应的证书是否过期。

## 11015001 签名异常

**错误信息**

Signature failed.

**错误描述**

签名验证失败，返回无效签名。

**可能原因**

签名验证或签名生成过程失败。

**处理步骤**

结合控制台输出的错误日志及命令行参数进一步分析。

## 11015002 证书与私钥不匹配

**错误信息**

Signature not matched.

**错误描述**

证书与私钥不匹配。

**可能原因**

profile文件签名使用的密钥与对应证书不匹配。

**处理步骤**

检查keyAlias参数指定的密钥与profileCertFile参数指定的证书是否匹配。

## 11015003 签名验证错误

**错误信息**

Verify signature failed.

**错误描述**

签名过程中，验证签名结果不匹配。

**可能原因**

1. 签名过程中的keyAlias密钥与appCertFile证书不匹配。
2. appCertFile指定的证书已过期。

**处理步骤**

1. 检查签名过程keyAlias指定的密钥与appCertFile指定的证书是否匹配。
2. 更新证书链文件。

## 11017001 软件包格式错误

**错误信息**

Read zip file failed.

**错误描述**

待签名的软件包格式错误。

**可能原因**

待签名的HAP/HSP/HNP软件包不符合zip规范：

1. 文件大小超过4GB；
2. 条目数（文件+目录）超过65535。

**处理步骤**

1. 减少软件包的大小，减少软件包的文件和目录数目。
2. 重新打包签名，确保打包格式为zip。

## 11017002 软件包复制异常

**错误信息**

Write zip file failed.

**错误描述**

复制待签名的HAP、HSP、HNP软件包异常。

**可能原因**

当前用户没有outFile参数指定的输出文件的写权限。

**处理步骤**

检查当前用户是否有outFile参数指定的输出文件的写权限。

## 11017003 HAP包字节对齐错误

**错误信息**

Alignment zip file failed

**错误描述**

HAP包字节对齐错误。

**可能原因**

HAP包字节对齐错误。

**处理步骤**

结合控制台输出的故障日志及应用包进一步分析。

## 11017004 待签名的软件包格式错误

**错误信息**

Zip format failed

**错误描述**

待签名的软件包格式错误。

**可能原因**

待签名的HAP、HSP、HNP软件包未满足zip格式规范（如压缩方式、文件结构等要求）。

**处理步骤**

重新打包签名。

## 11106001 无效的文件格式

**错误信息**

Invalid file format.

**错误描述**

输入文件格式错误。

**可能原因**

代码签名不支持输入的文件格式。

**处理步骤**

代码签名支持的文件格式为：hap、hsp、hqf。

## 11110001 文件流读取错误

**错误信息**

Input stream read error.

**错误描述**

文件读取错误。

**可能原因**

文件读取错误。

**处理步骤**

请重试，或结合故障日志及应用包进一步分析。

## 11111002 证书错误

**错误信息**

Certificates error.

**错误描述**

证书验证失败。

**可能原因**

1. 证书不正确。
2. 签名参数keyAlias的值不正确。

**处理步骤**

1. 检查证书格式内容是否正确。
2. 检查参数keyAlias的值是否正确。

## 11112001 Profile内容错误

**错误信息**

Profile content error.

**错误描述**

Profile内容错误。

**可能原因**

1. profile json内容格式不符合规范。
2. type缺失或值不合法。
3. bundle-info缺失。
4. app-identifier值类型错误或长度不合法。

**处理步骤**

1. 检查json内容结构是否符合格式规范。
2. 检查type值是否正确。
3. 补充bundle-info内容。
4. 确认app-identifier值类型为String，并且字符长度要求大于0、小于等于32。

## 11112002 module.json内容错误

**错误信息**

module.json content error.

**错误描述**

module.json文件内容错误。

**可能原因**

1. module.json内容格式不符合格式规范。
2. 应用包中hnp文件未在module.json中描述。

**处理步骤**

1. 检查json内容结构是否符合格式规范。
2. 在module.json中添加hnp文件描述，参考[开发指导](module-configuration-file.md#hnppackages标签)。

## 11112003 ELF文件错误

**错误信息**

ELF is incorrect.

**错误描述**

ELF文件解析错误。

**可能原因**

ELF文件的头信息错误。

**处理步骤**

检查ELF文件的头信息是否符合格式规范。

## 11112004 HNP文件错误

**错误信息**

Extract hnp file error.

**错误描述**

解压hnp文件错误。

**可能原因**

提取或解压hnp文件失败。

**处理步骤**

1. 再次执行签名。
2. 检查hnp文件打包是否正确。

## 11113001 算法错误

**错误信息**

Invalid algorithm.

**错误描述**

签名算法错误。

**可能原因**

安装的Java版本不支持此摘要算法。

**处理步骤**

代码签名需要SHA-256和SHA-512算法支持，请检查Java版本是否正确，当前支持Java8以上Java环境运行。

## 11114001 签名内部错误

**错误信息**

Code sign internal error.

**错误描述**

代码签名内部错误。

**可能原因**

工具签名过程中发生了内部错误。

**处理步骤**

结合故障日志及应用包进一步分析。

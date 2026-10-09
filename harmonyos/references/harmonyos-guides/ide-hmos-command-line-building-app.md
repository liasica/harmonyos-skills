---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-command-line-building-app
title: 搭建流水线
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 搭建流水线
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:490a1c79f449025eb94b6d9ec9eeafc7693987ff1350e57df4b1a9be81eca0a1
---

除了使用鸿蒙电脑DevEco Studio一键式构建应用/元服务外，还可以使用命令行工具来调用Hvigor任务进行构建。通过命令行的方式构建应用或元服务，可用于构建CI（Continuous Integration）流水线，按照计划时间自动化地构建HAP/APP、签名、安装运行等操作。

**说明** 

* HarmonyOS SDK已嵌入命令行工具中，无需额外下载配置。
* 请在执行命令行之前，保证当前工程是可信任的，确保安全编译。

## 系统平台要求

* HarmonyOS系统
* 内存：推荐使用32GB及以上
* 硬盘：100GB及以上

## 环境准备

### 获取命令行工具

1. [获取命令行工具](ide-hmos-commandline-get.md)。
2. 执行如下命令，解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，工具名称请根据实际情况进行修改。

   ```bash
   tar -zxvf commandline-tools-harmonyos-xxx.tar.gz
   ```
3. 将解压后所在的路径定义为COMMANDLINE\_TOOL\_DIR，在后续配置Node.js、hdc、hvigor等环境变量时使用。例如解压在用户根目录下。

   ```bash
   export COMMANDLINE_TOOL_DIR=~/command-line-tools
   ```

### 配置环境变量

配置Node.js、hvigor、hdc、sdk环境变量。

1. 添加环境变量。

   ```bash
   export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/node/bin         # 配置Node.js环境变量
   export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/hvigor/bin       # 配置hvigor环境变量
   export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/sdk/default/openharmony/toolchains      # 配置hdc环境变量
   export DEVECO_SDK_HOME=${COMMANDLINE_TOOL_DIR}/sdk         # 配置sdk环境变量
   ```
2. 执行如下命令，查询版本信息，确认配置成功。

   ```screen
   node -v
   hvigorw -v
   ohpm -v
   ```

### 配置npm镜像仓库

若您的工程在hvigor/hvigor-config.json5文件中依赖npm三方组件，流水线中则需要配置npm镜像地址，编译时才能正确地下载它。

```screen
npm config set registry https://repo.huaweicloud.com/repository/npm/
npm config set "@ohos:registry" https://repo.harmonyos.com/npm/
```

### 安装ohpm

1. 添加ohpm路径到环境变量，命令如下。

   ```bash
   export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/ohpm/bin
   ```
2. 执行如下命令，查询ohpm版本信息，确认配置成功。

   ```bash
   ohpm -v
   ```
3. 配置仓库地址（可指定多个地址，','号分割），指令如下。

   ```bash
   ohpm config set registry https://ohpm.openharmony.cn/ohpm/
   ohpm config set strict_ssl false
   ```

## 构建应用

### 安装工程及模块依赖

使用命令行进行构建前，需要分别进入工程及各个模块下执行ohpm install命令，安装**工程及各个模块**依赖的三方库。

1. 定义ohpm安装函数，示例如下。

   ```screen
   # 切换到指定目录$1并执行ohpm install指令
   function ohpm_install() {     
       cd $1              # $1：函数第一个参数, 必须是路径     
       ohpm install --all # 安装所有依赖
   }
   ```
2. 定义变量 **PROJECT\_PATH**，表示工程目录路径，示例如下。

   ```screen
   PROJECT_PATH=xxx/xxx/project_name  # 工程路径
   ```

   **注意** 

   工程目录不要存放在隐藏目录下，即工程路径的每一级目录中不要以.开头，例如xxx/.xxx/project，否则构建时可能会将模块中的代码和配置文件等作为资源打包进产物中，不会进行混淆或加密。
3. 安装工程及各个模块的三方库依赖，示例如下。

   ```screen
   # 根据业务情况安装ohpm三方库依赖
   ohpm_install "${PROJECT_PATH}"
   ```

### 执行Hvigor命令进行构建

使用hvigorw命令行工具执行构建命令，构建完成后，工程或模块下build目录中会生成相应的hap/hsp/har/app编译产物。

```screen
# 根据业务情况，执行相应的构建命令, 示例如下

# clean工程
hvigorw clean --no-daemon

# 构建Hap, 生成产物：${PROJECT_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/xxx.hap
hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon

# 构建Hsp, 生成产物：${PROJECT_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/(xxx.har | xxx.hsp)
hvigorw assembleHsp --mode module -p module=library@default -p product=default --no-daemon

# 构建Har, 生成产物：${PROJECT_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/outputs/xxx.har
hvigorw assembleHar --mode module -p module=library1@default -p product=default --no-daemon

# 构建App, 生成产物: ${PROJECT_PATH}/build/outputs/{productName}/xxx.app
hvigorw assembleApp --mode project -p product=default -p buildMode=debug --no-daemon
```

编译构建常见的任务和扩展参数如下，更多关于Hvigor命令行参数详见：[常用命令](ide-hmos-hvigor-commandline.md#section16300629103)。

**表1** HarmonyOS应用构建常用扩展参数

| 选项 | 说明 |
| --- | --- |
| -p buildMode={debug | release} | 采用debug/release模式进行编译构建。  缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。  关于构建模式的详细说明，请参考[指定构建模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)。针对HAR构建，请参考[构建HAR](ide-hmos-hvigor-build-har.md)。 |
| -p product={ProductName} | 指定product进行编译，编译product下配置的module target。  缺省时：默认为default。 |
| -p module={ModuleName}@{TargetName} | 指定模块及target进行编译，可指定多个相同类型的模块进行编译，以逗号隔开；TargetName不指定时默认为default。  限制：此参数需要与--mode module参数搭配使用。  缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。 |

**表2** HarmonyOS应用编译构建相关任务

| 选项 | 说明 |
| --- | --- |
| clean | 清理构建产物 |
| assembleHap | 构建Hap应用 |
| assembleApp | 构建App应用 |
| assembleHsp | 构建Hsp包 |
| assembleHar | 构建Har包 |

## 运行应用

如果工程级build-profile.json5中已配置[signingConfigs](ide-hmos-hvigor-build-profile-app.md#section153288223224)指定签名信息，并且流水线中存在签名文件（包括.cer、.p7b、.p12文件和material文件夹，material文件夹默认和.p12文件存放在同一路径下），构建后会分别生成已签名包（如xxx-signed.hap）和未签名包（如xxx-unsigned.hap），已签名包可直接在真机设备上运行，无需重新签名。如果需要对包进行重签名，可使用签名工具对未签名包进行签名，步骤如下。

### 准备申请签名所需文件

准备好申请签名所需3个文件：密钥（.p12文件）、数字证书（.cer文件）、Profile（.p7b文件）。

**生成密钥和证书请求文件**

使用签名工具hap-sign-tool生成密钥和证书请求文件，签名工具在${COMMANDLINE\_TOOL\_DIR}/sdk/default/openharmony/toolchains/lib下。

1. 在签名工具目录下，执行如下命令，生成密钥库文件。例如，生成的密钥库名称为demo.p12，存储到path目录下。

   ```screen
   hap-sign-tool generate-keypair -keyAlias debugKey -keyAlg ECC -keySize NIST-P-256 -keystoreFile /path/demo.p12 -keyPwd 123456Abc -keystorePwd 123456Abc
   ```

   关于该命令中需要修改的参数说明如下，其余参数不需要修改：

   * **keyAlias**：密钥的别名信息，用于标识密钥名称。
   * **keystoreFile**：密钥库文件，请将"/path/demo.p12"修改为实际路径。
   * **keyPwd** ：设置密钥密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **keystore****Pwd**：设置密钥库的密码，请与**keyPwd**保持一致。
2. 执行如下命令，生成证书请求文件。

   ```screen
   hap-sign-tool generate-csr -keyAlias debugKey -signAlg SHA256withECDSA -subject "CN=debugKey,OU=HUAWEI IDE,O=HUAWEI,L=guangzhou,ST=guangdong,C=CN" -keystoreFile /path/demo.p12 -outFile /path/demo.csr -keyPwd 123456Abc -keystorePwd 123456Abc
   ```

   生成证书请求文件的参数说明如下：

   * **keyAlias**：与上一步骤中输入的**keyAlias**保持一致。
   * **subject**: 证书主题。
     + CN：名称与姓氏，建议与别名一致。
     + OU：组织单位名称，如HUAWEI IDE。
     + O：组织名称，如HUAWEI。
     + L：所在城市、地区。
     + ST：省份。
     + C：国家/地区代码，如CN。
   * **keystoreFile**：与上一步骤中输入的**keystoreFile**保持一致。
   * **outFile**：生成的证书请求文件名称，后缀为.csr，请将"/path/demo.csr"修改为实际路径。
   * **keyPwd**：密钥口令，与上一步骤中输入的**keyPwd**保持一致。
   * **keystorePwd**：密钥库口令，与上一步骤中输入的**keystorePwd**保持一致。

**申请调试****数字证书和Profil****e****文件**

生成证书请求文件后，在AppGallery Connect中申请、下载调试数字证书和Profile文件，具体请参考[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)和[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

### 对未签名的HAP/APP进行签名

1. 使用签名工具hap-sign-tool进行签名，签名工具在${COMMANDLINE\_TOOL\_DIR}/sdk/default/openharmony/toolchains/lib下。
2. 在签名工具目录下，使用如下命令进行签名。详细的签名工具指导请参考[Hap包签名工具](https://gitcode.com/openharmony/developtools_hapsigner)。

   ```screen
   hap-sign-tool sign-app -mode localSign -keystoreFile /path/demo.p12 -keystorePwd 123456Abc -keyAlias debugKey -keyPwd 123456Abc -signAlg SHA256withECDSA -profileFile /path/demo.p7b -appCertFile /path/demo.cer -inFile /path/hap-unsigned.hap -outFile /path/hap-signed.hap
   ```

   关于该命令中需要修改的参数说明如下，其余参数不需要修改：

   * **keystoreFile**：密钥库文件，格式为.p12。
   * **keystorePwd**：密钥库密码。
   * **keyAlias**：密钥别名。
   * **keyPwd**：密钥密码。
   * **profileFile**：申请的调试Profile文件，格式为.p7b。
   * **appCertFile**：申请的调试证书文件，格式为.cer。
   * **inFile**：通过Hvigor打包生成的未携带签名信息的HAP。
   * **outFile**：经过签名后生成的携带签名信息的HAP。

   **说明** 

   如果要对APP进行签名，只需将**inFile**和**outFile**参数修改为APP包即可。

### 运行应用

通过[hdc工具](hdc.md)将HAP推送到真机设备上进行安装，需要注意的是，推送的HAP必须是携带签名信息的，否则会导致HAP安装失败。

推送HAP的命令如下：

```screen
# 将打包好的hap包推送至设备中
hdc file send "{PROJECT_PATH}/entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
# 安装hap包
hdc shell bm install -p "data/local/tmp/entry-default-signed.hap"
# 删除hap包
hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"
```

在设备上运行HAP的命令如下：

```screen
hdc shell aa start -a EntryAbility -b com.example.myapplication -m entry
```

## 示例脚本

**说明** 

此脚本无法直接运行，仅供参考，业务要根据自己的情况来进行适配。

```bash
#!/bin/sh
set -ex

COMMANDLINE_TOOL_DIR=xxx/command-line-tools #命令行工具的安装目录

# 配置Node.js、hvigor、ohpm、hdc等环境变量
export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/node/bin 
export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/hvigor/bin
export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/ohpm/bin
export PATH=$PATH:${COMMANDLINE_TOOL_DIR}/sdk/default/openharmony/toolchains
export DEVECO_SDK_HOME=${COMMANDLINE_TOOL_DIR}/sdk

# 配置ohpm仓库地址
function init_ohpm() {
    ohpm -v  
    ohpm config set registry https://ohpm.openharmony.cn/ohpm/
}

# 初始化相关路径
PROJECT_PATH=xxx  # 工程目录
# 进入package目录安装依赖
function ohpm_install {
    cd $1
    ohpm install
}
# 环境适配
function buildHAP() {
    # 根据业务情况安装ohpm三方库依赖
    ohpm_install "${PROJECT_PATH}"
    ohpm_install "${PROJECT_PATH}/entry"
    ohpm_install "${PROJECT_PATH}/xxx"
    # 根据业务情况，采用对应的构建命令，可以参考DevEco Studio构建日志中的命令
    cd ${PROJECT_PATH}
    hvigorw clean --no-daemon
    hvigorw assembleHap --mode module -p product=default -p debuggable=false --no-daemon # 流水线构建命令建议末尾加上--no-daemon
}
function install_hap() {
    hdc file send "${PROJECT_PATH}/entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
    hdc shell bm install -p "data/local/tmp/entry-default-signed.hap" 
    hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"
    hdc shell aa start -a MainAbility -b com.example.myapplication -m entry
}

# 使用ohpm发布har
function upload_har {
  ohpm publish pkg.har
}

function main {
  local startTime=$(date '+%s')
  init_ohpm
  buildHAP
  install_hap
  upload_har
  local endTime=$(date '+%s')
  local elapsedTime=$(expr $endTime - $startTime)
  echo "build success in ${elapsedTime}s..."
}
main
```

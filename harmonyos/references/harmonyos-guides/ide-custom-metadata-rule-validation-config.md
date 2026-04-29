---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-metadata-rule-validation-config
title: 自定义元数据规则校验插件配置
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义元数据规则校验插件 > 自定义元数据规则校验插件配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:55+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:bb463ae5068e4d926c5202843521db7b06827557a0c5c161cc9b0b50cdcc4e0a
---

ohpm-repo 5.1.3版本开始支持自定义元数据规则校验，允许通过插件对oh-package.json5中部分字段开发定制化的校验规则。

注意

自定义元数据规则校验插件的作用是基于原有元数据校验规则的增强，而非替换，原有校验规则可参考[oh-package.json5规格文档](ide-oh-package-json5.md)。

## 准备工作

1. 下载ohpm-repo5.1.3及以上版本工具安装包并解压。
2. 根据[模板文件](ide-rule-verification-template-file.md)中的操作指示，创建三个必要模板文件：[checkField.ts](ide-rule-verification-template-file.md#section14072085013)，[CustomExtensionValidationConfig.json](ide-rule-verification-template-file.md#section1076523392)和[tsconfig.json](ide-rule-verification-template-file.md#section1613602518915)。
3. 将文件[tsconfig.json](ide-rule-verification-template-file.md#section1613602518915)文件移动到ohpm-repo解压根目录内；建议将文件[checkField.ts](ide-rule-verification-template-file.md#section14072085013)和[CustomExtensionValidationConfig.json](ide-rule-verification-template-file.md#section1076523392)文件移动到ohpm-repo解压根目录的plugins/fieldCheckPlugin文件夹内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/kX3ofwTcQUW7y50GMykAtQ/zh-cn_image_0000002561831175.png?HW-CC-KV=V1&HW-CC-Date=20260429T054453Z&HW-CC-Expire=86400&HW-CC-Sign=D9EF6BCD19284A02D1C59D62FC12A1753B5AB25DDC7D7837027D6CAF709BA2D1)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/BS7iS7JTReSz0kkVXmJ5BQ/zh-cn_image_0000002530911254.png?HW-CC-KV=V1&HW-CC-Date=20260429T054453Z&HW-CC-Expire=86400&HW-CC-Sign=33E4E41A08550CC814AD11226995A4D20F921CD1EC21ED329F7B0064F024E43B "点击放大")

## 编写自定义规则校验函数文件checkField.ts

打开[checkField.ts](ide-rule-verification-template-file.md#section14072085013)模板文件（默认名称为checkField，可自定义修改），创建与文件同名的校验函数（示例：文件checkField.ts中仅允许存在一个名称为checkField的函数），实现自定义规则校验函数接口ValidationExtensionRule。若需定义多个校验规则，需要为每个规则创建专属的校验函数文件。

```
1. // 自定义规则校验函数接口ValidationExtensionRule定义如下
2. export interface ValidationExtensionRule {
3. (fieldData: FieldDataType, userInfo: UserBasicInfo): void;
4. }
```

1. 入参：包含两个固定入参：
   * fieldData：oh-package.json5文件中字段的取值，类型可以是布尔值，字符串，字符串数组，对象和对象数组。
   * userInfo：发布三方包用户的信息，包含userName和userRole两部分：
     + userInfo.userName：字符串类型，发布三方包账户的用户名称。
     + userInfo.userRole：字符串类型，发布三方包账户的用户角色，1表示为管理员账户，0表示为普通用户（使用[自定义认证插件](ide-custom-auth-plugin.md)，默认为0）。
2. 返回值：字段校验成功返回void，校验失败则抛出错误并返回错误原因。

规则校验函数实现过程中需要引用UserBasicInfo，FieldDataType类型和ValidationExtensionRule接口，处理函数报错时将会使用日志记录、异常处理等基础功能，需准确书写函数引用路径。相关工具类与方法具体使用方法见[checkField.ts](ide-rule-verification-template-file.md#section14072085013)模板文件，存放位置如下：

* FieldDataType和ValidationExtensionRule：FieldDataType为字段信息类型，ValidationExtensionRule为规则函数的接口，地址：<ohpm-repo解压根目录>/libs/service/validator/validationExtensionRule/ValidationExtensionRule.js。
* UserBasicInfo：用户信息类型，地址：<ohpm-repo解压根目录>/libs/service/validator/validationExtensionRule/type.js。
* CustomValidateError：错误抛出类，地址：<ohpm-repo解压根目录>/libs/service/validator/CustomValidateError.js。
* OhpmLazyLogger：日志打印类，地址为：<ohpm-repo解压根目录>/libs/packages/log。

## 编写自定义规则配置文件CustomExtensionValidationConfig.json

完成自定义规则校验函数开发后，需要在模板文件[CustomExtensionValidationConfig.json](ide-rule-verification-template-file.md#section1076523392)中（该文件名不可自定义），为oh-package.json5文件中需要被加强校验的字段配置所需的校验规则。

```
1. [
2. {
3. "attrName": "<被校验字段的名称1>",
4. "configs": [
5. {
6. "ruleType": "规则的类型，不配置默认为CustomFunction",
7. "description": "<规则的功能描述>",
8. "ruleContent": "<规则的内容>"
9. },
10. {
11. "ruleType": "规则的类型，不配置默认为CustomFunction",
12. "description": "<规则的功能描述>",
13. "ruleContent": "<规则的内容>"
14. }
15. ]
16. },
17. {
18. "attrName": "<被校验字段的名称2>",
19. "configs": [
20. {
21. "ruleType": "规则的类型，不配置默认为CustomFunction",
22. "description": "<规则的功能描述>",
23. "ruleContent": "<规则的内容>"
24. },
25. {
26. "ruleType": "规则的类型，不配置默认为CustomFunction",
27. "description": "<规则的功能描述>",
28. "ruleContent": "<规则的内容>"
29. }
30. ]
31. }
32. ]
```

* attrName：被校验字段的名称，支持模块级oh-package.json5中所有字段进行校验，也支持自定义字段（例如在三方包的oh-package.json5中添加一个自定义字段A，可以对字段A进行校验）。

  注意

  oh-package.json5中author字段分为'author.name'，'author.email'，'author.url'三个字段独立校验。attrName不能重复，重复将报错。
* configs：被校验字段的规则配置，一个attrName对应一个configs，configs可包含多个config，每个config对应一个独立规则，config配置有三个参数：
  + ruleType：表示字段的规则类型，string类型，不配置默认为“CustomFunction”，规则类型有六种：["CustomFunction","NotNull","LengthLimit","ListItemLengthLimit","MapEntry","RegExp"]，当使用“CustomFunction”时需要编写自定义校验规则函数文件，其他五种规则类型配置即生效，系统已经完成功能实现。
    - CustomFunction：自定义函数规则。
    - NotNull：非空规则。
    - LengthLimit：字符串长度限制规则。
    - ListItemLengthLimit：字符串数组中单个字符串长度限制规则。
    - MapEntry：对象数据校验规则，可以对key和value进行不同的规则校验。
    - RegExp：字符串正则匹配校验。
  + description：string类型，规则的功能描述，内容不做校验。
  + ruleContent：规则的内容，具体格式要求需与ruleType相匹配。

## CustomExtensionValidationConfig.json中六种字段规则校验

根据ruleType的不同，ohpm-repo提供六种字段校验能力：

1. 自定义函数校验：CustomFunction
   * 规则配置：

     ```
     1. [
     2. {
     3. "attrName": "<oh-package.json5文件的字段名称>",
     4. "configs": [
     5. {
     6. "ruleType": "CustomFunction",
     7. "description": "自定义规则校验",
     8. "ruleContent": "<自定义规则函数的名称>"
     9. }
     10. ]
     11. }
     12. ]
     ```

     + ruleType如果不配置，将默认为CustomFunction。
     + ruleContent必须是字符串类型，值为自定义规则函数的名称（示例：书写规则函数文件checkField.ts，ruleContent取值为checkField）。
2. 非空校验：NotNull
   * 规则配置：

     ```
     1. [
     2. {
     3. "attrName": "<oh-package.json5文件的字段名称>",
     4. "configs": [
     5. {
     6. "ruleType": "NotNull",
     7. "description": "非空校验",
     8. "ruleContent": ""
     9. }
     10. ]
     11. }
     12. ]
     ```

     + 当字段配置规则为非空时，会校验字段是否为空或者长度是否为0，ruleContent必须保持为空字符串。

3. 长度校验：LengthLimit

   * 规则配置：

     ```
     1. [
     2. {
     3. "attrName": "<oh-package.json5文件的字段名称>",
     4. "configs": [
     5. {
     6. "ruleType": "LengthLimit",
     7. "description": "字符串长度校验",
     8. "ruleContent": {
     9. "minLength": <最小长度>,
     10. "maxLength": <最大长度>
     11. }
     12. }
     13. ]
     14. }
     15. ]
     ```
   * 字段需要是字符串类型，例如字段name，对字段长度进行限制，长度范围为[最小长度，最大长度]，长度为整数类型，可以仅配置minLength或者maxLength，minLength和maxLength需要为非负数，且maxLength需要大于等于minLength。

4. 数组长度校验：ListItemLengthLimit
   * 规则配置：

     ```
     1. [
     2. {
     3. "attrName": "<oh-package.json5文件的字段名称>",
     4. "configs": [
     5. {
     6. "ruleType": "ListItemLengthLimit",
     7. "description": "数组中单个字符串长度校验",
     8. "ruleContent": {
     9. "maxLength": <最大长度>,
     10. "minLength": <最小长度>
     11. }
     12. }
     13. ]
     14. }
     15. ]
     ```
   * 字段需要是字符串数组类型，例如字段keywords，对数组中每一个字符串的长度进行限制，长度范围为[最小长度，最大长度]，长度为整数类型，可以只配置minLength或者maxLength，minLength和maxLength需要为非负数，且maxLength大于等于minLength。

5. Map对象类型校验：MapEntry
   * 规则配置：

     ```
     1. [
     2. {
     3. "attrName": "<oh-package.json5文件的字段名称>",
     4. "configs": [
     5. {
     6. "ruleType": "MapEntry",
     7. "description": "Map中单个key-value的字符校验",
     8. "ruleContent": {
     9. "keyRuleConfig": {
     10. "ruleType": <key值规则校验类型>,
     11. "ruleContent": <key值规则校验内容>
     12. },
     13. "valueRuleConfig": {
     14. "ruleType": <value值规则校验类型>,
     15. "ruleContent":<value值规则校验内容>
     16. }
     17. }
     18. }
     19. ]
     20. }
     21. ]
     ```
   * 字段需要是对象类型，例如字段dependencies，针对对象中每一组数据的key和value值分别做校验，key和value需要同时配置。
     + keyRuleConfig：有两个参数，ruleType和ruleContent，规格同[configs](ide-custom-metadata-rule-validation-config.md#li1678919385917)中的[ruleType](ide-custom-metadata-rule-validation-config.md#li278918315598)和[ruleContent](ide-custom-metadata-rule-validation-config.md#li157891933595)，定义key值的校验规则。
     + valueRuleConfig：有两个参数，ruleType和ruleContent，规格同[configs](ide-custom-metadata-rule-validation-config.md#li1678919385917)中的[ruleType](ide-custom-metadata-rule-validation-config.md#li278918315598)和[ruleContent](ide-custom-metadata-rule-validation-config.md#li157891933595)，定义value值的校验规则。

6. 正则校验：RegExp
   * 规则配置：

     ```
     1. [
     2. {
     3. "attrName": "<oh-package.json5文件的字段名称>",
     4. "configs": [
     5. {
     6. "ruleType": "RegExp",
     7. "description": "字符串正则表达校验",
     8. "ruleContent": <正则表达式>
     9. }
     10. ]
     11. }
     12. ]
     ```
   * 字段需要是字符串类型，例如字段name，对字段内容进行正则匹配限制，ruleContent需为有效的正则表达式。

## 启用自定义规则配置

为了保证ohpm-repo能够正确加载自定义规则校验，需要修改配置文件config.yaml，开启自定义元数据规则校验，涉及field\_check\_plugin字段内容修改。

```
1. field_check_plugin:
2. config_file_path:  plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json
3. check_func_dir: plugins/fieldCheckPlugin
```

参数说明：

* config\_file\_path：字段校验配置文件路径，支持绝对路径和相对路径，相对路径的基准为ohpm-repo解压根目录，建议将文件存放在软件包的plugins/fieldCheckPlugin目录下，默认值为plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json。
* check\_func\_dir：字段校验函数文件所在目录路径，支持绝对路径和相对路径，相对路径的基准为ohpm-repo解压根目录，建议将目录设置为plugins/fieldCheckPlugin文件夹，默认值为plugins/fieldCheckPlugin。

## 使用自定义规则校验

1. 安装必要的npm包。

   通过命令行工具，在ohpm-repo解压根目录下，安装typescript包和@types/node包。

   ```
   1. $ npm i typescript
   2. $ npm i @types/node
   ```
2. 编译自定义规则函数文件。

   如果checkField.ts（举例说明，函数名称可自定义）存放在ohpm-repo安装根目录的plugins/fieldCheckPlugin文件夹中，当编写完规则函数后，通过命令行工具，在ohpm-repo安装根目录下执行如下编译命令。

   ```
   1. $ tsc
   ```

   命令成功执行后会在ohpm-repo解压根目录的plugins/outDir文件夹中生成编译后的文件checkField.js。

   如果checkField.ts没有存放在plugins/fieldCheckPlugin内，请先修改[tsconfig.json](ide-rule-verification-template-file.md#section1613602518915)文件中参数include和outDir，include指定需编译的插件代码的存储目录，outDir指定编译后文件的存储位置，修改后通过命令行工具，在ohpm-repo解压根目录下执行编译命令“tsc”。

   ```
   1. // tsconfig.json 文件中的默认配置
   2. // 默认值：自定义规则函数文件默认存放在 ./plugins/fieldCheckPlugin 中，编译后的文件存放在./plugins/outDir中
   3. "include": "plugins/fieldCheckPlugin/*"          // 插件文件的位置
   4. "outDir": "./plugins/outDir"                     // 编译后文件的存放位置
   ```
3. 编译后文件指定存放位置。

   编译后获得的checkField.js需要与checkField.ts保持在同一级目录中，否则会编译出错。默认checkField.js文件输出在./plugins/outDir内，需要把checkField.js拷贝到checkField.ts同级目录./plugins/fieldCheckPlugin中（ohpm-repo成功启动后可删除checkField.ts文件）。
4. ohpm-repo服务的启动。

   在完成上述操作之后，通过执行[install](ide-ohpm-repo-install.md)和[start](ide-ohpm-repo-start.md)命令，完成服务的部署启动。
5. 发布三方包，使用自定义规则校验。

   通过ohpm命令行工具或者ohpm-repo管理界面，发布三方包。在发包的过程中包的元数据将通过自定义规则的校验，如果校验不通过则会报错，请根据报错信息修改oh-package.json文件的内容再重新发布三方包。

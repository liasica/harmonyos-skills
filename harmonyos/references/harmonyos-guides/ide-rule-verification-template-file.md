---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-rule-verification-template-file
title: 模板文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义元数据规则校验插件 > 模板文件
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:55+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5427ce42589c6f6b96782e71931c05b43556392d6f0349f2299af138368864ad
---

模板文件中包含自定义元数据规则校验插件需要的三个文件：自定义规则校验函数模板文件checkField.ts，自定义规则校验配置模板文件CustomExtensionValidationConfig.json和ts编译为js的配置模板文件tsconfig.json。

请创建指定名称的文件，并把下方源码拷贝到文件中。

## 自定义规则校验函数模板文件checkField.ts

```
1. //如果自定义校验规则文件checkField.ts存储在默认位置（ohpm-repo解压根目录的plugins/fieldCheckPlugin文件夹内），插件文件checkField.ts中默认工具类引用地址如下
2. import {
3. FieldDataType,
4. ValidationExtensionRule
5. } from '../../libs/service/validator/validationExtensionRule/ValidationExtensionRule';
6. import {UserBasicInfo} from '../../libs/service/validator/validationExtensionRule/type';
7. import {CustomValidateError} from '../../libs/service/validator/CustomValidateError';
8. import {OhpmLazyLogger as log} from '../../libs/packages/log';
9. /**
10. * 自定义规则校验
11. * @param fieldData 字段的取值
12. * @param userInfo 发布三方包用户的信息，包含userName和userRole两部分
13. *    userInfo.userName：发布三方包账户的用户名称
14. *    userInfo.userRole：发布三方包账户的用户角色，1表示为管理员账户，0表示为普通用户
15. */
16. export const checkField: ValidationExtensionRule = (fieldData: FieldDataType, userInfo: UserBasicInfo): void => {
17. const name: string = <string>fieldData;      // 待校验字段的值，以name为例
18. const userName: string = userInfo.userName;  // 发布三方包账户的用户名称
19. const userRole: number = userInfo.userRole;  // 发布三方包账户的用户角色，1表示为管理员账户，0表示为普通用户
20. // 错误抛出分为两部分：CustomValidateError第一个参数内容将打印在ohpm-repo运行日志中（命令行和ohpm-repo管理界面发布三方包均会打印），第二个参数内容将打印在ohpm-repo管理界面弹窗（仅限ohpm-repo管理界面发布三方包）
21. if (name === 'package') {
22. throw new CustomValidateError('Cannot publish package named "package"',
23. '不能发布包名为package的包');
24. }
25. // 成功日志打印，日志级别打印可以为：log.trace，log.debug，log.info，log.warn和log.error
26. log.info('校验成功');  // log.debug('校验成功');
27. };
```

## 自定义规则校验配置模板文件CustomExtensionValidationConfig.json

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

## ts编译为js的配置模板文件tsconfig.json

```
1. // tsconfig.json 文件指定了编译项目所需的根目录下的文件以及编译选项，编译自定义插件文件 .ts 为 .js文件。
2. {
3. "include": [
4. "plugins/fieldCheckPlugin/*" // 插件文件的位置
5. ],
6. "compilerOptions": {
7. "target": "es2016",
8. "experimentalDecorators": true,
9. "emitDecoratorMetadata": true,
10. "module": "commonjs",
11. "rootDirs": [
12. "./src",
13. "./test"
14. ],
15. "typeRoots": [
16. "./node_modules/@types"
17. ],
18. "types": [
19. "node",
20. ],
21. "resolveJsonModule": true,
22. "outDir": "./plugins/outDir",   // 编译后文件输出的位置
23. "esModuleInterop": true,
24. "forceConsistentCasingInFileNames": true,
25. "alwaysStrict": true,
26. "noImplicitReturns": true,
27. "skipLibCheck": true
28. }
29. }
```

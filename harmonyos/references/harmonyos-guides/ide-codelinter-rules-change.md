---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codelinter-rules-change
title: 规则变更说明
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 规则变更说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:04baaa70849a39291fe2c44d3564969c2c58ea114f9f9a3cbbe5b3d288ddf4c8
---

## 6.1.0.609

新增规则

* [@performance/custom-node-memory-leak-check](ide-custom-node-memory-leak-check.md)
* [@performance/state-variable-usage-in-ui-format-check](ide-state-variable-usage-in-ui-format-check.md)
* [@correctness/multimedia-use-stride-in-image-receiver](ide-multimedia-use-stride-in-image-receiver.md)
* [@correctness/v1-nested-object-property-change-format-check](ide-v1-nested-object-property-change-format-check.md)
* [@correctness/v1-state-object-member-used-in-function-parameter-check](ide-v1-state-object-member-used-in-fun-parameter.md)

## 6.0.2.636

新增规则

* [@correctness/redundant-dependency-check](ide-redundant-dependency-check.md)
* [@cross-device-app-dev/immersive-effect-check](ide-immersive-effect-check.md)

## 6.0.1.246

新增规则

* [@compatibility/api-compatibility-check](ide-api-compatibility-check.md)

## 6.0.0.848

新增规则

* [@security/no-unsafe-kdf](ide_no-unsafe-kdf.md)
* [@security/no-unsafe-sm4](ide_no-unsafe-sm4.md)
* [@security/no-unsafe-sm2-key](ide_no-unsafe-sm2-key.md)
* [@security/no-unsafe-sm2-cipher](ide_no-unsafe-sm2-cipher.md)
* [@security/no-unsafe-ecdh](ide_no-unsafe-ecdh.md)
* [@security/no-unsafe-huks](ide_no-unsafe-huks.md)

## 6.0.0.828

新增规则

* [@performance/no-use-any-import](ide-no-use-any-import.md)
* [@performance/avoid-overusing-custom-component-check](ide-avoid-overusing-custom-component-check.md)
* [@performance/bad-deep-clone-check](ide-bad-deep-clone-check.md)
* [@performance/reasonable-audio-use-check](ide-reasonable-audio-use-check.md)
* [@performance/reasonable-sensor-use-check](ide-reasonable-sensor-use-check.md)
* [@performance/reasonable-gps-use-check](ide-reasonable-gps-use-check.md)
* [@performance/reuse-date-instances-check](ide-reuse-date-instances-check.md)
* [@performance/crypto-replacement-check](ide-crypto-replacement-check.md)
* [@performance/monitor-invisible-area-in-image-animation](ide-monitor-invisible-area-in-image-animation.md)
* [@performance/datashare-query-unrelease-check](ide-datashare-query-unrelease-check.md)
* [@performance/dark-color-mode-check](ide-dark-color-mode-check.md)
* [@performance/update-state-var-between-animatetos-check](ide-update-state-var-between-animatetos-check.md)
* [@performance/tabs-on-change-check](ide-tabs-on-change-check.md)
* [@performance/nested-post-frame-callback-check](ide-nested-post-frame-callback-check.md)
* [@cross-device-app-dev/window-size-change-listener-check](ide-window-size-change-listener-check.md)

## 6.0.0.418

新增规则

* [@performance/web-on-active-check](ide-web-on-active-check.md)
* [@performance/gif-hardware-decoding-check](ide-gif-hardware-decoding-check.md)
* [@cross-device-app-dev/one-multi-breakpoint-check](ide-one-multi-breakpoint-check.md)

变更规则

* [@typescript-eslint/explicit-function-return-type](ide_explicit-function-return-type.md)规则新增额外选项allowArkTS（默认为false），配置为true时，支持对.ets文件进行检查。

## 5.1.0.828

新增规则

* [@performance/web-cache-mode-check](ide-performance-web-cache-mode-check.md)
* [@correctness/audio-interrupt-check](ide-audio-interrupt-check.md)
* [@correctness/audio-pause-or-mute-check](ide-audio-pause-or-mute-check.md)
* [@correctness/avsession-metadata-check](ide-avsession-metadata-check.md)
* [@correctness/avsession-buttons-check](ide-avsession-buttons-check.md)
* [@correctness/image-interpolation-check](ide-image-interpolation-check.md)
* [@correctness/image-pixel-format-check](ide-image-pixel-format-check.md)
* [@performance/hp-ffrt-no-use-std](ide-hp-ffrt-no-use-std.md)

变更规则

* [@performance/hp-arkui-use-taskpool-for-web-request](ide-hp-arkui-use-taskpool-for-web-request.md)所属规则集由recommended改为all。

## 5.0.7.100

新增规则

* [@performance/foreach-index-check](ide-foreach-index-check.md)
* [@performance/js-code-cache-by-precompile-check](ide-js-code-cache-by-precompile-check.md)
* [@performance/js-code-cache-by-interception-check](ide-js-code-cache-by-interception-check.md)
* [@performance/init-list-component](ide-init-list-component.md)
* [@correctness/listen-default-network-change](ide_listen-default-network-change.md)
* [@correctness/listen-multi-network-concurrent](ide_listen-multi-network-concurrent.md)
* [@security/no-unsafe-3des](ide-no-unsafe-3des.md)

变更规则

* [@performance/high-frequency-log-check](ide-high-frequency-log-check.md)增加检测高频函数onWillScroll。
* [@typescript-eslint/prefer-readonly-parameter-types](ide_prefer-readonly-parameter-types.md)和[@typescript-eslint/no-magic-numbers](ide_no-magic-numbers.md)中，规则的默认告警级别由error改为warn。
* [@typescript-eslint/lines-between-class-members](ide_lines-between-class-members.md)默认检查规则从成员变量之间必须有空行分隔，变更为成员变量和成员变量之间不需要有空行分隔。
* [@security/no-unsafe-hash](ide_no-unsafe-hash.md)新增对@ohos/crypto-js包中不安全Hash算法检查。
* [@security/no-unsafe-mac](ide_no-unsafe-mac.md)新增对@ohos/crypto-js包中不安全Mac算法检查。

## 5.0.5.200

变更规则

* [@performance/hp-arkui-avoid-empty-callback](ide_hp-arkui-avoid-empty-callback.md)所属规则集由recommended改为all。
* [@performance/hp-arkui-use-word-break-to-replace-zero-width-space](ide_hp-arkui-use-word-break-in-space.md)所属规则集由recommended改为all。
* [@performance/hp-arkui-remove-redundant-nest-container](ide_hp-arkui-no-redundant-nest.md)所属规则集由recommended改为all。
* [@performance/hp-arkui-remove-container-without-property](ide_hp-arkui-remove-container-without-property.md)所属规则集由recommended改为all。
* [@performance/sparse-array-check](ide-sparse-array-check.md)所属规则集由recommended改为all。
* [@performance/number-init-check](ide-number-init-check.md)所属规则集由recommended改为all。
* [@performance/typed-array-check](ide-typed-array-check.md)所属规则集由recommended改为all。

## 5.0.3.800

**新增规则**

* [@performance/hp-arkui-reduce-pangesture-distance](ide-hp-arkui-reduce-ges-distance.md)
* [@performance/hp-arkui-suggest-use-get-anonymousid-async](ide-hp-arkui-sg-anonymousid-async.md)
* [@performance/multiple-associations-state-var-check](ide-multi-associations-state-var-check.md)
* [@performance/constant-property-referencing-check-in-loops](ide-constant-property-check-in-loops.md)
* [@performance/foreach-args-check](ide-foreach-args-check.md)

**变更规则**

* [@security/specified-interface-call-chain-check](ide-specified-interface-call-chain-check.md)新增对命名空间namespace、类型别名type、接口interface、枚举enum和结构体struct的支持。namespace字段配置类型从字符串变更为数组。

* [@performance/high-frequency-log-check](ide-high-frequency-log-check.md)默认告警等级从suggestion变更为warn，该规则新增至all规则集中。
* [@performance/number-init-check](ide-number-init-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/start-window-icon-check](ide-start-window-icon-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/sparse-array-check](ide-sparse-array-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/typed-array-check](ide-typed-array-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/waterflow-data-preload-check](ide-waterflow-data-preload-check.md)该规则新增至recommended规则集中。
* [@performance/hp-arkts-no-use-any-export-current](ide-hp-arkts-no-use-any-export-current.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkts-no-use-any-export-other](ide-hp-arkts-no-use-any-export-other.md)，该规则新增至recommended规则集中。
* [@performance/hp-arkui-avoid-empty-callback](ide_hp-arkui-avoid-empty-callback.md)告警级别由warn改为suggestion。
* [@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse](ide_hp-arkui-abouttoreuse.md)，该规则新增至recommended规则集中。
* [@performance/hp-arkui-image-async-load](ide_hp-arkui-image-async-load.md)所属规则集由recommend改为all。
* [@performance/hp-arkui-load-on-demand](ide_hp-arkui-load-on-demand.md)告警级别由suggestion改为warn。
* [@performance/hp-arkui-no-stringify-in-lazyforeach-key-generator](ide_hp-arkui-no-stringify-lazyforeach-key.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-remove-container-without-property](ide_hp-arkui-remove-container-without-property.md)告警级别由warn改为suggestion。
* [@performance/hp-arkui-remove-redundant-nest-container](ide_hp-arkui-no-redundant-nest.md)告警级别由warn改为suggestion。
* [@performance/hp-arkui-replace-nested-reusable-component-by-builder](ide_hp-arkui--replace-reusable-by-builder.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-suggest-cache-avplayer](ide-hp-arkui-suggest-cache-avplayer.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component](ide_hp-arkui-use-reuseid-if-else-component.md)告警级别由suggestion改为warn, 该规则新增至recommended规则集中。
* [@performance/hp-arkui-suggest-use-effectkit-blur](ide-hp-arkui-suggest-use-effectkit-blur.md)，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-grid-layout-options](ide_hp-arkui-use-grid-layout-options.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-local-var-to-replace-state-var](ide_hp-arkui-use-local-var-to-replace-state-var.md)告警级别由suggestion改为warn。
* [@performance/hp-arkui-use-onAnimationStart-for-swiper-preload](ide_hp-arkui-use-onanimationstart-in-swiper.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-reusable-component](ide_hp-arkui-use-reusable-component.md)告警级别由suggestion改为warn。
* [@performance/hp-arkui-use-row-column-to-replace-flex](ide_hp-arkui-use-row-column-to-replace-flex.md)，所属规则集由recommended改为all。
* [@performance/hp-arkui-use-scale-to-replace-attr-animateto](ide_hp-arkui-use-scale-to-replace-attr-animateto.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-taskpool-for-web-request](ide-hp-arkui-use-taskpool-for-web-request.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-transition-to-replace-animateto](ide_hp-arkui-use-transition-to-replace-animateto.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-word-break-to-replace-zero-width-space](ide_hp-arkui-use-word-break-in-space.md)该规则新增至recommended规则集中。
* [@performance/hp-arkui-set-cache-count-for-lazyforeach-grid](ide_hp-arkui-set-cache-count-for-lazyforeach-grid.md)告警级别由warn改为suggestion。

**下线规则**

* [@performance/hp-arkui-wrap-waterflow-if-else-footer](ide-hp-arkui-wrap-waterflow-if-else-footer.md)

## 5.0.3.600

**新增规则**

* [@performance/hp-arkui-wrap-waterflow-if-else-footer](ide-hp-arkui-wrap-waterflow-if-else-footer.md)
* [@performance/hp-arkui-remove-unchanged-state-var](ide-hp-arkui-remove-unchanged-state-var.md)
* [@performance/hp-arkts-no-use-any-export-current](ide-hp-arkts-no-use-any-export-current.md)
* [@performance/hp-arkts-no-use-any-export-other](ide-hp-arkts-no-use-any-export-other.md)
* [@performance/hp-arkui-suggest-cache-avplayer](ide-hp-arkui-suggest-cache-avplayer.md)
* [@performance/hp-arkui-suggest-use-effectkit-blur](ide-hp-arkui-suggest-use-effectkit-blur.md)
* [@performance/lottie-animation-destroy-check](ide-lottie-animation-destroy-check.md)
* [@performance/timezone-interface-check](ide-timezone-interface-check.md)

**变更规则**

以下规则的部分场景，在5.0.3.600之前的版本检查执行Codelinter检查时不报错，升级至DevEco Studio 5.0.3.600版本后执行Codelinter检查将报错。

* [@typescript-eslint/no-unnecessary-condition](ide_no-unnecessary-condition.md)

```
1. // 场景一：支持逻辑表达式的检查
2. interface GeneratedTypeLiteralInterface {}
3. declare let foo: GeneratedTypeLiteralInterface;
4. foo ??= 1; // 升级前不报错，升级后报错
5. // 场景二：链式表达式中可以推断为非空的场景下，不需要增加判空
6. interface GeneratedTypeLiteralInterface {
7. bar: () => number;
8. }
9. type Foo = GeneratedTypeLiteralInterface | null;
10. declare const foo: Foo;
11. foo?.bar()?.toExponential(); // 升级前不报错，升级后报错
```

* [@typescript-eslint/promise-function-async](ide_promise-function-async.md)

```
1. // 函数返回值没有显式定义类型，并且返回值可能为Promise的场景下，函数需要定义为async
2. function promiseInUnionWithoutExplicitReturnType(p: boolean) { // 升级前不报错，升级后报错
3. return p ? Promise.resolve(5) : 5;
4. }
```

* [@typescript-eslint/member-ordering](ide_member-ordering.md)

```
1. // 配置了optionalityOrder选项，并且类属性中不包含可选变量的场景下，规则中配置的order选项在历史版本中失效了
2. // 规则配置为"@typescript-eslint/member-ordering": ["error", {"default": {"memberTypes": 'never', "order": 'natural-case-insensitive', "optionalityOrder": 'required-first',}}]
3. class X {
4. b: string = '';
5. a: string = ''; // 升级前不报错，升级后报错
6. }
```

* [@typescript-eslint/naming-convention](ide_naming-convention.md)

```
1. // 支持检查interface中的typeMethod
2. // 规则配置为："@typescript-eslint/naming-convention": ["error", {selector: 'typeMethod', format: ['PascalCase']}]
3. interface SOME_INTERFACE {
4. someMethod: () => void; // 升级前不报错，升级后报错
5. some_property: string;
6. }
```

* [@typescript-eslint/ban-types](ide_ban-types.md)

```
1. // 支持检查extend、implements后的类型
2. // 规则配置为："@typescript-eslint/ban-types": ["error",{"types": {"Bar": {"message": ""}}}]
3. interface Bar {}
4. interface Baz {}
5. interface Foo extends Bar, Baz {} // 升级前不报错，升级后报错
```

* [@typescript-eslint/no-floating-promises](ide_no-floating-promises.md)

```
1. // 场景一：.finally()被认为是没有有效处理Promise中可能发生的异常
2. Promise.reject().finally(() => {}) // 升级前不报错，升级后报错
3. // 场景二：.then()中的第二个参数如果是undefined或者null，被认为是没有有效处理Promise中可能发生的异常
4. Promise.resolve().then(() => {}, undefined); // 升级前不报错，升级后报错
5. Promise.resolve().then(() => {}, null); // 升级前不报错，升级后报错
```

* [@typescript-eslint/no-inferrable-types](ide_no-inferrable-types.md)

```
1. // 支持检查构造函数中的参数类型
2. class Foo {
3. constructor(param: boolean = true) {} // 升级前不报错，升级后报错
4. }
```

* [@typescript-eslint/prefer-readonly](ide_prefer-readonly.md)

```
1. interface GeneratedObjectLiteralInterface {
2. prop?: string
3. }

5. class Test {
6. // 支持检查私有属性
7. #testObj: GeneratedObjectLiteralInterface = {}; // 升级前不报错，升级后报错

9. public test(): void {
10. this.#testObj?.prop;
11. }
12. }
```

## 5.0.3.500

**新增规则**

* [@security/no-unsafe-dh-key](ide_no-unsafe-dh-key.md)
* [@security/no-unsafe-dsa-key](ide_no-unsafe-dsa-key.md)
* [@security/no-unsafe-rsa-key](ide_no-unsafe-rsa-key.md)
* [@performance/hp-arkui-use-attributeUpdater-control-refresh-scope](ide-hp-attribute-update-refresh-scope.md)
* [@performance/hp-arkui-use-id-in-get-resource-sync-api](ide_hp-arkui-use-id-in-get-resource-sync-api.md)
* [@performance/hp-arkui-use-transition-to-replace-animateto](ide_hp-arkui-use-transition-to-replace-animateto.md)
* [@performance/hp-arkui-remove-redundant-state-var](ide-hp-arkui-remove-redundant-state-var.md)
* [@performance/hp-arkui-use-taskpool-for-web-request](ide-hp-arkui-use-taskpool-for-web-request.md)
* [@security/specified-interface-call-chain-check](ide-specified-interface-call-chain-check.md)
* [@hw-stylistic/file-naming-convention](ide-file-naming-convention.md)

**变更规则**

* @performance/high-frequency-log-check所属规则集由all变更为recommended。

**下线规则**

* [@performance/object-creation-check](ide-object-creation-check.md)
* [@performance/hp-arkui-limit-refresh-scope](ide_hp-arkui-limit-refresh-scope.md)
* [@performance/lazyforeach-args-check](ide-lazyforeach-args-check.md)

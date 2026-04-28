---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-486
title: 自定义组件内定义方法报错，出现异常的原因
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义组件内定义方法报错，出现异常的原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:08+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:6bb7587a258f37456926d2fce026b0c6d86378fd91eb20633144425e649a2a15
---

**问题现象**

@Component中定义一些框架的方法与开发者在@Component中定义的方法重名，导致框架中的方法被override，可能会导致出现报错“is not callable”或应用异常。

**解决措施**

为避免出现开发者在自定义组件中定义的方法跟自定义组件框架的方法重名，导致运行时异常，开发者可参考如下表格，凡是在表格中被列出来的，开发者需要将其定义成不同的名字，以防止运行时功能异常。

| 自定义组件已定义的方法或属性名 | | | |
| --- | --- | --- | --- |
| isRenderInProgress | isInitialRenderDone | runReuse\_ | paramsGenerator\_ |
| watchedProps | recycleManager\_ | hasBeenRecycled\_ | preventRecursiveRecycle\_ |
| delayRecycleNodeRerender | delayRecycleNodeRerenderDeep | defaultConsume\_ | reconnectConsume\_ |
| providedVars\_ | dirtyElementIdsNeedsUpdateSynchronously\_ | localStoragebackStore\_ | ownObservedPropertiesStore\_\_ |
| get ownObservedPropertiesStore\_ | obtainOwnObservedProperties | get localStorage\_ | set localStorage\_ |
| get isViewV2() | aboutToBeDeleted | aboutToBeDeletedInternal | purgeDeleteElmtId |
| purgeVariableDependenciesOnElmtIdOwnFunc | debugInfoStateVars | initAllowComponentFreeze | setActiveInternal |
| onActiveInternal | onInactiveInternal | purgeVariableDependenciesOnElmtId | initialRender |
| rerender | updateRecycleElmtId | updateStateVars | initialRenderView |
| UpdateElement | delayCompleteRerender | flushDelayCompleteRerender | forceRerenderNode |
| collectElementsNeedToUpdateSynchronously | viewPropertyHasChanged | uiNodeNeedUpdateV2 | performDelayedUpdate |
| declareWatch | addProvidedVar | findProvidePU\_\_ | initializeConsume |
| reconnectToConsume | disconnectedConsume | markElemenDirtyById | updateDirtyElements |
| observeComponentCreation | observeComponentCreation2 | getOrCreateRecycleManager | getRecycleManager |
| hasRecycleManager | initRecycleManager | rebuildUpdateFunc | observeRecycleComponentCreation |
| aboutToReuseInternal | stopRecursiveRecycle | aboutToRecycleInternal | recycleSelf |
| isRecycled | UpdateLazyForEachElements | createStorageLink | createStorageProp |
| createLocalStorageLink | createLocalStorageProp | debugInfoView | debugInfoViewInternal |
| debugInfoDirtyDescendantElementIds | debugInfoDirtyDescendantElementIdsInternal | \_\_mkRepeatAPI | reuseOrCreateNewComponent |
| dirtDescendantElementIds\_ | monitorIdsDelayedUpdate | monitorIdsDelayedUpdateForAddMonitor\_ | computedIdsDelayedUpdate |
| recyclePoolV2\_ | resetStateVarsOnReuse | aboutToReuseInternals | aboutToRecycleInternal |
| freezeRecycledComponent | unfreezeReusedComponent | getOrCreateRecyclePool | getRecyclePool |
| hasRecyclePool | cleanupRecycledElmtId | get isViewV2 | purgeDeleteElmtId |
| aboutToBeDeletedInternal | initialRenderView | resetMonitorsOnReuse | resetComputed |
| resetConsumer | observeComponentCreation2 | initParam | updateParam |
| resetParam | uiNodeNeedUpdateV2 | updateDirtyElements | UpdateElement |
| getViewV2ChildById | addDelayedMonitorIdsForAddMonitor | addDelayedComputedIds | setActiveInternal |
| performDelayedUpdate | findProvidePU\_\_ | get localStorage\_() | reuseOrCreateNewComponent |
| debugInfoDirtDescendantElementIdsInternal | debugInfoStateVars | \_\_mkRepeatAPI | debugInfoView |
| debugInfoViewInternal | debugInfoDirtDescendantElementIds | observeRecycleComponentCreation | debugInfo\_\_ |
| recycleSelf | finalizeConstruction | hasBeenRecycled\_ | paramsGenerator\_ |
| inactiveComponents\_ | get isReusable\_() | compareNumber | currentlyRenderedElmtIdStack\_ |
| dirtDescendantElementIds\_ | dirtRetakenElementIds\_ | parent\_ | renderingPaused |
| isDeleting\_ | isCompFreezeAllowed\_ | prebuildFuncQueues | propertyChangedFuncQueues |
| extraInfo\_ | \_\_isBlockRecycleOrReuse\_\_ | elmtIdsDelayedUpdate\_ | prebuildPhase\_ |
| isPrebuilding\_ | prebuildingElmtId\_ | doRecycle | doReuse |
| nativeViewPartialUpdate | create | createRecycle | markNeedUpdate |
| syncInstanceId | restoreInstanceId | getInstanceId | markStatic |
| finishUpdateFunc | setCardId | getCardId | elmtIdExists |
| isLazyItemRender | isFirstRender | findChildByIdForPreview | resetRecycleCustomNode |
| queryNavDestinationInfo | queryNavigationInfo | queryRouterPageInfo | getUIContext |
| sendStateInfo | getUniqueId | setIsV2 | getDialogController |
| allowReusableV2Descendant | id\_\_() | updateId | scheduleDelayedUpdate |
| get elmtIdsDelayedUpdate | setParent | getParent | removeChild |
| aboutToBeDeleted | isDeleting | setDeleting | setDeleteStatusRecursively |
| isCompFreezeAllowed | setActiveCount | getChildViewV2ForElmtId | purgeVariableDependenciesOnElmtIdOwnFunc |
| debugInfo\_\_ | debugInfoRegisteredElmtIds | debugInfoElmtIds | dumpStateVars |
| debugInfoStateVars | isViewActive | purgeVariableDependenciesOnElmtId | initialRender |
| rerender | get isViewV2 | updateRecycleElmtId | updateStateVars |
| UpdateElement | dumpReport | forceCompleteRerender | \_\_ClearAllRecycle\_\_PUV2ViewBase\_\_Internal |
| forceRerenderNode | hasNodeUpdateFunc | pauseRendering | restoreRendering |
| forEachUpdateFunction | getNodeById | getCurrentlyRenderedElmtId | debugInfoViewHierarchy |
| debugInfoUpdateFuncByElmtId | debugInfoUpdateFuncByElmtIdInternal | debugInfoInactiveComponents | \_\_mkRepeatAPI |
| findViewInHierarchy | onDumpInfo | printDFXHeader | processOnDumpCommands |
| traverseChildDoRecycleOrReuse | processPropertyChangedFuncQueue | setPrebuildPhase | isNeedBuildPrebuildCmd |
| prebuildComponent | isEnablePrebuildInMultiFrame | ifElseBranchUpdateFunctionDirtyRetaken | onDumpInspector |
| prebuildPhase\_ | activeCount\_ | isView\_ | childrenWeakrefMap\_ |
| builderNodeWeakrefMap\_ | updateFuncByElmtId | id\_ | shareLocalStorage\_ |
| \_\_parentViewBuildNode\_\_ | \_\_enableBuilderNodeConsume\_\_ | \_\_elmtId2Repeat\_\_\_ | arkThemeScopeManager |
| ifElseBranchUpdateFunctionDirtyRetaken | forceCompleteRerender | forceRerenderNode | purgeDeleteElmtId |
| findProvidePU\_\_ | id\_\_() | debugInfo\_\_() | debugInfoElmtId |
| getChildById | addChild | setParentBuilderNode\_\_ | addChildBuilderNode |
| propagateToChildrenToConnected | removeChildBuilderNode | clearChildBuilderNode | propagateToChildrenToDisconnected |
| purgeDeletedElmtIds | updateStateVarsOfChildByElmtId | createOrGetNode | ifElseBranchUpdateFunction |
| setArkThemeScopeManager | onWillApplyThemeInternally | getShareLocalStorage | setShareLocalStorage |
| propagateToChildren | setActiveInternal |  |  |

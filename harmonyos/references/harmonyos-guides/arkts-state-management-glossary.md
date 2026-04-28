---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-glossary
title: 状态管理术语
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理术语
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:68a8e81a98369b30baadf4f346dbc236e52276ded56b34ce4ef01458894e9eb0
---

## A

### 属性级精准更新（Attribute-Level Updates）

状态管理框架使用类属性装饰器可以实现对类对象中属性的观测能力，当属性发生变化时，只刷新该属性绑定的组件，其他未发生变化的属性绑定的组件将不会被连带刷新。

## D

### 数据源/同步源（Data Source）

状态变量的原始来源，可以同步给不同的状态数据。通常为父组件传给子组件的数据。

### 深度监听（Deep Monitor）

@Monitor装饰器用于监听数据的变化，深度监听会递归监听对象或数组的所有嵌套属性。

### 深度观察（Deep Observation）

深度观察能力指的是UI能够递归观察到对象或数组的所有嵌套属性。

## L

### 本地初始化（Local Initialization）

在变量声明的时候赋值，作为变量的默认值。

## M

### 标脏（Mark Dirty）

当状态变量发生变化时，框架会将依赖于该变量的系统组件以及该变量所属的自定义组件标记为“脏”。在后续UI渲染的过程中，会将标脏的节点重新[刷新](arkts-state-management-introduce.md#触发更新)。

### 最小化更新（Minimum Updates）

最小化更新是UI框架的一种优化策略，确保只更新实际发生变化的部分，即只刷新与发生变化的状态变量绑定的系统组件，避免不必要的渲染操作。

## N

### 命名参数机制（Named Parameter Mechanism）

父组件通过指定参数传递给子组件的状态变量，为父子传递同步参数的主要手段。

## O

### 一层监听（One-Layer Monitor）

@Watch装饰器用于监听数据的变化，一层监听只能监听对象或数组的第一层属性的变化，不会递归监听嵌套属性。

### 一层观察（One-Layer Observation）

UI能够观察到@State、@Prop等V1装饰器装饰的状态变量一层属性的变化。

### 单向同步（One-Way Sync）

数据只能从一个方向流动，通常是从父组件到子组件。子组件可以接收父组件的数据，但不能直接修改父组件的数据源。

## R

### 引用传递（Reference Transmission）

在函数调用或变量赋值时，传递的是变量本身，包含[收集依赖](arkts-state-management-introduce.md#收集依赖)和[触发更新](arkts-state-management-introduce.md#触发更新)的逻辑。

### 常规变量（Regular Variables）

没有被状态装饰器装饰的变量，通常应用于辅助计算。它的改变永远不会引起UI的刷新。

### 渲染过程（Render Phase）

渲染过程是状态管理[触发更新](arkts-state-management-introduce.md#触发更新)流程中的一个阶段，指组件[标脏](arkts-state-management-glossary.md#标脏mark-dirty)完成后，下一帧信号到来时刷新UI的这段流程。在此过程中，框架遍历脏自定义组件列表，调用系统生成的rerender方法，遍历脏系统组件，刷新组件并更新依赖。

## S

### 状态变量（State Variables）

被状态装饰器装饰的变量，状态变量值的改变会引起UI的渲染更新。

## T

### 尾随闭包（Trailing Lambda）

尾随闭包是ArkTS中的一种语法特性，当闭包作为函数的最后一个参数时，可以将该闭包表达式写在函数调用括号之后，以提高代码可读性。

### 双向同步（Two-way Sync）

数据可以在两个方向上流动，父子组件可以相互修改。

## V

### 值传递（Value Transmission）

在函数调用或变量赋值时，传递的是变量的值，而非变量本身，不包含收集依赖和触发更新的逻辑。

### 视图（View）

视图指的是UI界面。

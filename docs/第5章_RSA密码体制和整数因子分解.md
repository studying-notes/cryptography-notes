---
date: 2022-01-28T08:48:26+08:00  # 创建日期
author: "Rustle Karl"  # 作者

# 文章
title: "第5章_RSA密码体制和整数因子分解"  # 文章标题
# description: "文章描述"
url:  "posts/cryptography/docs/第5章_RSA密码体制和整数因子分解"  # 设置网页永久链接
tags: ["密码学"]  # 标签
series: [ "密码学学习笔记"]  # 系列
categories: [ "学习笔记"]  # 分类

# 章节
weight: 20 # 排序优先级
chapter: false  # 设置为章节

index: true  # 是否可以被索引
toc: true  # 是否自动生成目录
draft: false  # 草稿
---

## 5.1 公钥密码学简介

公钥密码体制无法提供无条件安全性。

把公钥密码体制抽象为一种称为陷门单向函数（trapdoor one-way function）的抽象。

尽管有很多单射函数被认为是单向的，但是还没有一个函数能被证明是单向的。

## 5.3 RSA 密码体制

![](../assets/images/密码体制5.1_RSA密码.png)

RSA 密码体制的安全性是基于相信加密函数是一个单向函数这一事实，所以，对于一个敌手来说试图解密密文将是计算上不可行的。

## 5.3.1 实现 RSA

![](../assets/images/算法5.4_RSA参数生成.png)

## 5.4 素性检测


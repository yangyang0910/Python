# -*- coding:utf-8 -*-
# AUTHER   @ Alvin.

'''
infolist方法返回的是一个ZipInfo对象列表
  getinfo方法只返回一个ZipInfo对象，表示zip文档中相应文件的信息。
ZipInfo的属性：
  ZipInfo.filename：获取文件名称
  ZipInfo.date_time：获取文件最后修改时间。返回一个包含6个元素的元组：(年, 月, 日, 时, 分, 秒)
  ZipInfo.compress_type：压缩类型。
  ZipInfo.comment：文档说明
  ZipInfo.extr：扩展项数据
  ZipInfo.create_system：获取创建该zip文档的系统
  ZipInfo.create_version：创建zip文档的PKZIP版本
  ZipInfo.extract_version：获取解压zip文档所需的PKZIP版本
  ZipInfo.reserved：预留字段，当前实现总是返回0
  ZipInfo.flag_bits：zip标志位
  ZipInfo.volume：文件头的卷标
  ZipInfo.internal_attr：内部属性
  ZipInfo.external_attr：外部属性
  ZipInfo.header_offset：文件头偏移位
  ZipInfo.CRC：未压缩文件的CRC-32
  ZipInfo.compress_size：获取文件压缩后的大小
  ZipInfo.file_size：获取未压缩的文件大小
'''


'''
tarfile.is_tarfile(filename):判断文件是否是一个tar归档文件
getmember(filename):返回对象成员名称，如果那个成员名不能被发现，将引发一个keyerror
getmembers():返回归档成员属性的详细信息的对象，相当于zipfile里面的infolist
                      name:文件名字，getnames()也能返回文件名
                      mode：权限
                      mtime：创建时间
                      size：文件的大小，bytes
list():返回成员存档对象 相当于ls -l
extract('filename','path'):解压单个文件到指定路径
extractfile(filename):可以访问归档成员的数据，如果成员是文件的话可以用read()读取文件类容（文件的方法）
extractall('path'):解压全部文件到指定路径，解压单个文件到指定目录的方法是extractall('path',member=t.getmember(filename))
'''
import zipfile
z = zipfile.ZipFile("E:\\Python\\模块二\\day06\\new.zip", "r")
print(z.extractall("E:\Python\模块二\day06\\new"))
z.close()
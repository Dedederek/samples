"""
Copyright (R) @huawei.com, all rights reserved
-*- coding:utf-8 -*-
"""
import acl
from constants import ACL_ERROR_NONE, ACL_MEM_MALLOC_HUGE_FIRST
from constants import ACL_MEMCPY_DEVICE_TO_DEVICE, ACL_MEMCPY_HOST_TO_DEVICE, ACL_MEMCPY_DEVICE_TO_HOST

def check_ret(message, ret):
    """check_ret"""
    if ret != ACL_ERROR_NONE:
        raise Exception("{} failed ret={}"
                        .format(message, ret))


def copy_data_device_to_host(device_data, data_size):
    """copy_data_device_to_host"""
    host_buffer, ret = acl.rt.malloc_host(data_size)
    if ret != ACL_ERROR_NONE:
        print("Malloc host memory failed, error: ", ret)
        return None

    ret = acl.rt.memcpy(host_buffer, data_size,
                        device_data, data_size,
                        ACL_MEMCPY_DEVICE_TO_HOST)
    if ret != ACL_ERROR_NONE:
        print("Copy device data to host memory failed, error: ", ret)
        acl.rt.free_host(host_buffer)
        return None

    return host_buffer


def copy_data_device_to_device(device_data, data_size):
    """copy_data_device_to_device"""
    device_buffer, ret = acl.rt.malloc(data_size, ACL_MEM_MALLOC_HUGE_FIRST)
    if ret != ACL_ERROR_NONE:
        print("Malloc device memory failed, error: ", ret)
        return None

    ret = acl.rt.memcpy(device_buffer, data_size,
                        device_data, data_size,
                        ACL_MEMCPY_DEVICE_TO_DEVICE)
    if ret != ACL_ERROR_NONE:
        print("Copy device data to device memory failed, error: ", ret)
        acl.rt.free(device_buffer)
        return None

    return device_buffer


def copy_data_host_to_device(host_data, data_size):
    """copy_data_host_to_device"""
    device_buffer, ret = acl.rt.malloc(data_size, ACL_MEM_MALLOC_HUGE_FIRST)
    if ret != ACL_ERROR_NONE:
        print("Malloc device memory failed, error: ", ret)
        return None

    ret = acl.rt.memcpy(device_buffer, data_size,
                        host_data, data_size,
                        ACL_MEMCPY_HOST_TO_DEVICE)
    if ret != ACL_ERROR_NONE:
        print("Copy device data to device memory failed, error: ", ret)
        acl.rt.free(device_buffer)
        return None

    return device_buffer


def align_up(value, align):
    """align_up"""
    return int(int((value + align - 1) / align) * align)


def align_up16(value):
    """align_up16"""
    return align_up(value, 16)


def align_up2(value):
    """dvpp align_up2"""
    return align_up(value, 2)


def yuv420sp_size(width, height):
    """yuv420sp_size"""
    return int(width * height * 3 / 2)
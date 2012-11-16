# -*- coding: utf-8 -*-

import sys
import xml.dom.minidom

def compare_two_files(params):

    """
         src_file  - translated file
         dst_file  - file for translation
         base_file - usually english lang
    """

    src_file = params.get('argv', [])[1]
    dst_file = params.get('argv', [])[2]

    src = get_dic(xml.dom.minidom.parse(src_file))
    dst = get_dic(xml.dom.minidom.parse(dst_file))

    src_set = set(src.keys())
    dst_set = set(dst.keys())
    in_src_only = src_set - dst_set
    return in_src_only


def get_dic(doc):
    res = {}
    for node in doc.getElementsByTagName("string"):
        try:
            if len(node.childNodes):
                l = len(node.childNodes)
                if l:
                    res[node.getAttribute("name")] = node.childNodes[0].data
            else:
                res[node.getAttribute("name")] = ''
        except:
            print("Error key: %s" % node.getAttribute("name"))
    return res

def check_repo(params):
    #base_dic = get_dic(xml.dom.minidom.parse(base_file))
    return True


def parse_parameters(argv):
    return {'command': "compare", 'argv': argv}

def print_diff(params, diff):
    base_file = params.get('argv', [])[3]
    base = get_dic(xml.dom.minidom.parse(base_file))
    print ("%s and %s have %d differences:" % (params.get('argv', [])[2], params.get('argv', [])[1], len(diff)))
    for e in diff:
        print('  <string name="%s">%s</string>' % (e, base.get(e, '')))

def main():

    params = parse_parameters(sys.argv)
    command = params.get('command')

    # check translation repo
    if command == 'check':
        check_repo(params)

    # comapre two xmls	   
    if command == 'compare':
        diff = compare_two_files(params)
        print_diff(params, diff)

main()
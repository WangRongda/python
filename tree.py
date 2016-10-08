#!/usr/bin/python3

def print_tree(tree):
	buff = ['ROOT/']
	_print_tree(tree, buff, '', 0)
	buff = ('\n'.join(buff))
	print buff.encode("utf-8")

def _print_tree(tree, buff, prefix, level):
	count = len(tree)
	tr = tree.items()
	tr = sorted(tr, key=lambda tr : tr[0])
	for k, v in tr:
		count -= 1
		if isinstance(v, dict):
			buff.append('%s +- %s/' % (prefix, k))
			if count > 0:
				_print_tree(v, buff, prefix + ' |  ', level + 1)
			else:
				_print_tree(v, buff, prefix + '    ', level + 1)
		else:
			buff.append('%s +- %s : %s' % (prefix, k, v))

def test():
		print_tree(tree)

if __name__ == '__main__':
	test()

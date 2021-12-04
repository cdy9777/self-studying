from data_structure import ds_BST


class AVL(ds_BST.BST):
    def rotationRight(self, z):
        if not z:
            return 0
        x = z.left
        if x == None:
            return 0
        b = x.right
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.right = z
        z.parent = x
        z.left = b
        if b:
            b.parent = z
        if z == self.root:
            self.root = x

    def rotationLeft(self, z):
        if not z:
            return 0
        x = z.right
        if x == None:
            return 0
        b = x.left
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.left = z
        z.parent = x
        z.right = b
        if b:
            b.parent = z
        if z == self.root:
            self.root = x

    def rebalance(self, x, y, z):
        if y == z.left and x == y.left:
            self.rotationRight(z)
        elif y == z.right and x == y.right:
            self.rotationLeft(z)
        elif y == z.left and x == y.right:
            self.rotationLeft(y)
            self.rotationRight(z)
        else:
            self.rotationRight(y)
            self.rotationLeft(z)
        return x  # 이게 맞나..?

    def balanced_factor(self, x):
        return x.right.height - x.left.hegiht
        # child_node = x
        # while True:
        #     if child_node.right or child_node.left:
        #         x.height += 1
        #         if self.balanced_factor(child_node.right) > self.balanced_factor(child_node.left):
        #             child_node = child_node.right
        #         else:
        #             child_node = child_node.left
        #     else:
        #         break
        # return x.height

    def insert(self, key):
        v = super(AVL, self).insert(key)
        x = v
        next = x
        while True:
            if self.balanced_factor(x) >= -1 and self.balanced_factor(x) <= 1:
                next = x.parent
                continue
            else:
                z = next
                if v.key > z:
                    y = z.right
                    if v.key > y.key:
                        x = y.right
                    else:
                        x = y.left
                else:
                    y = z.left
                    if v.key > y.key:
                        x = y.right
                    else:
                        x = y.left
                break
        w = self.rebalance(x, y, z)
        if w.parent == None:
            self.root = w

    def delete(self, u):
        v = super(AVL, self).deleteByMerging(u)
        while v != None:
            # TODO: update v.height
            if self.balanced_factor(v) < 2 and self.balanced_factor(v) > -2:
                z = v
                if z.left.height > z.right.height:
                    y = z.left
                else:
                    y = z.right
                if y.left.height > y.right.height:
                    x = y.left
                else:
                    x = y.right
                v = self.rebalance(x, y, z)
            w = v
            v = v.parent
        self.root = w

# TODO LIST
# TODO: height 조정하는 코드 추가

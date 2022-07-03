HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    return int(pos%10 == 8) + num_eights(pos//10) if pos != 0 else 0


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    # In this function, we may define a helper function to track some var
    def helper(index, value, dir):
        if index == n:
            return value
        else:
            if index % 8 == 0 or num_eights(index) > 0:
                return helper(index+1, value-dir, -dir)
            else: return helper(index+1, value+dir, dir)
    return helper(1, 1, 1)

def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def func(num_change, n):
        """Copied from somewhere
        func(num_change, n)表示: 在使用面额大于等于n的硬币的条件下, 有几种兑换num_change的方法
        with_max 表示继续使用面额为n的硬币进行找零
        notwith_max 表示不再使用面额为n的硬币, 之后只能使用面额更大的硬币进行找零
        中心思想: 为了避免重复计算, 要用with_max和notwith_max分开计算两种情况下的找零方法,
        否则会有重复计算的风险. 事实上也可以使用func(change, 25), 只不过在func里就要用get_smaller_coin
        """
        if num_change == 0:
            return 1
        elif num_change < 0 or n == None:
            return 0
        else:
            notwith_max = func(num_change, get_larger_coin(n))
            with_max = func(num_change - n, n)
            print("DEBUG:", num_change, n, with_max, notwith_max)
            return with_max + notwith_max
    return func(change, 1)
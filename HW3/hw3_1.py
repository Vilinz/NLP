def editdis(str1, str2):
  len_str1 = len(str1) + 1
  len_str2 = len(str2) + 1
  # 一维数组来标记扣分
  matrix = [0 for n in range(len_str1*len_str2)]

  # 初始化
  for i in range(len_str1):
    matrix[i] = i
  for j in range(0, len(matrix), len_str1):
    if j % len_str1 == 0:
      matrix[j] = j

  for i in range(1, len_str1):
    for j in range(1, len_str2):
      if str1[i-1] == str2[j-1]:
        cost = 0
      else:
        cost = 1
      matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1 + i] + 1, 
                                matrix[j*len_str1 + (i - 1)] + 1,
                                matrix[(j - 1)*len_str1 + (i - 1)] + cost)
  return matrix[-1]

def main():
  str1 = input("The first string:")
  str2 = input("The second string:")
  print(editdis(str1, str2))


if __name__ == '__main__':
  main()

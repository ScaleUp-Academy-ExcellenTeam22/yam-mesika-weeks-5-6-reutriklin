def interleave(*parameters):
  listReturn=[]
  for i,element in enumerate(parameters):
    for param in parameters:
      listReturn+=[param[i]]
  return listReturn


#interleave('abc', [1, 2, 3], ('!', '@', '#'))
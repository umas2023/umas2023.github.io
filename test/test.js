function findMethod(chokoNum,nutList){
  let nutLength = nutList.length
  let dp = new Array(n).fill(0)
  dp[0] = 0
  dp[1] = 1
  for(let n=2;n<nutLength;i++){
      for(let i=0;i<n;i++)
      dp[n] = dp[i]+dp[n-i]
  }
  return dp[netLength]
}

function linearSearch(searchTerm, arr) {
  for(let i = 0; i < arr.length; i++){
    if(arr[i] === searchTerm){
      return i;
    }
  }
  return undefined;
}

function globalLinearSearch(searchTerm, arr) {
  let results = []
  for(let i = 0; i < arr.length; i++){
    if(arr[i] === searchTerm){
      results.push(i)
    }
  }
  return results;
}

module.exports = { linearSearch, globalLinearSearch };

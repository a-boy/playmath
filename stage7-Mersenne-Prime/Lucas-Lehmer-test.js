/**
 * Lucas-Lehmer 检验函数
 */
function isMersennePrime(p) {
  if (p < 2) return false;
  if (p === 2) return true;
  if (p % 2 === 0) return false; // 除2外的偶数指数对应的梅森数必为合数

  const pBI = BigInt(p);
  const TWO = BigInt(2);
  const M_p = TWO ** pBI - BigInt(1);

  let s = BigInt(4);

  // 迭代 p-2 次
  for (let i = 0; i < p - 2; i++) {
    // 使用 BigInt 取模
    s = (s * s - TWO) % M_p;
  }

  return s === BigInt(0);
}

// --- 命令行输入处理 ---

// process.argv[2] 获取命令行第一个参数
const input = process.argv[2];

if (!input) {
  console.error("错误: 请提供一个整数 p 作为参数。");
  console.log("用法: node lucas.js <p>");
  process.exit(1);
}

const p = parseInt(input);

if (isNaN(p) || p <= 0) {
  console.error("错误: 参数 p 必须是一个正整数。");
  process.exit(1);
}

console.log(`正在检验 M${p} (2^${p} - 1)...`);
console.time("计算耗时");

const result = isMersennePrime(p);

console.timeEnd("计算耗时");
console.log(`结果: M${p} ${result ? "是" : "不是"} 素数。`);

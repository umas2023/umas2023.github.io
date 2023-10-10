async function processTasks(taskList, n) {
    const results = [];
    let currentIndex = 0;

    // 执行单个任务
    async function runTask(task, taskIndex) {
        const result = await task();
        results[taskIndex] = result;
    }

    // 滑动窗口
    async function runTasksInWindow() {
        while (currentIndex < taskList.length) {
            const taskIndex = currentIndex++;
            const task = taskList[taskIndex];
            await runTask(task, taskIndex);
        }
    }

    // 并行任务
    const runningTasks = [];
    for (let i = 0; i < n; i++) {
        runningTasks.push(runTasksInWindow());
    }

    await Promise.all(runningTasks);
    return results;
}

// 示例使用

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const createTask = (taskName, duration) => {
    return new Promise((resolve) => {
        console.log(`starting task ${taskName}`);
        delay(duration).then(() => {
            console.log(`complete task ${taskName}`);
            resolve(taskName);
        });
    });
};

const taskList = [
    () => createTask("task1", 1000),
    () => createTask("task2", 1000),
    () => createTask("task3", 1000),
    () => createTask("task4", 1000),
];

//这段代码是一个立即执行的异步函数表达式（Immediately Invoked Async Function Expression，IIFE）
// 在这里，定义了一个匿名的异步函数，并立即执行它
(async () => {
    const results = await processTasks(taskList, 2);
    console.log(results);
})();
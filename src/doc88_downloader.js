/*
使用說明：
    1. 先手動瀏覽全部頁數，讓每頁內容都成功被載入
    2. 在瀏覽器按下 F12 進入開發者模式
    3. 複製貼上此份 js 程式碼
    4. 修改頁數範圍
    5. 按下 Enter 執行
*/

function downloadPages(from, to) {
    for (i = from; i <= to; i++) {
        const pageCanvas = document.getElementById('page_' + i);
        if (pageCanvas === null) { break; }
        const pageNo = parseInt(String(i));
        setTimeout(() => {
            console.log("==pageNo==>>", pageNo);
            ((num) => {
                console.log("开始打印第" + num + "页");
                pageCanvas.toBlob(
                    blob => {
                        const anchor = document.createElement('a');
                        anchor.download = 'page_' + num + '.png';
                        anchor.href = URL.createObjectURL(blob);
                        anchor.click();
                        URL.revokeObjectURL(anchor.href);
                    }
                );
            })(pageNo);
        }, 500 * pageNo);
    }
}

downloadPages(1, 40)

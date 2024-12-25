/**
 * Function Description: Downloads all pages within the specified page range and saves each page as a PNG image.
 * Steps to use:
 * 1. Manually browse through all the pages to ensure that the content on each page is loaded.
 * 2. Open developer mode (F12) and paste this code into the Console.
 * 3. Modify the page range (from, to).
 * 4. Press Enter to execute.
 *
 * @param {number} startPage - The starting page number.
 * @param {number} endPage - The ending page number.
 */
function downloadPages(startPage, endPage) {
    // Loop through the page range
    for (let pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
        // Get the corresponding canvas element for the page
        const pageCanvas = document.getElementById('page_' + pageNumber);

        // If the page doesn't exist, stop the loop
        if (pageCanvas === null) {
            console.error(`Canvas element for page ${pageNumber} not found.`);
            break;
        }

        // Set delay time to avoid rapid requests
        const delayTime = 500 * pageNumber;

        // Set a timeout to delay the download of the page image
        setTimeout(() => {
            downloadPageAsImage(pageCanvas, pageNumber);
        }, delayTime);
    }
}


/**
 * Downloads the specified page's canvas as a PNG image.
 *
 * @param {HTMLCanvasElement} canvas - The canvas element for the page.
 * @param {number} pageNumber - The page number.
 */
function downloadPageAsImage(canvas, pageNumber) {
    console.log(`Starting download of page ${pageNumber}...`);

    // Convert the canvas to a Blob and download
    canvas.toBlob(blob => {
        if (!blob) {
            console.error(`Failed to convert page ${pageNumber} to Blob.`);
            return;
        }

        const downloadLink = document.createElement('a');
        downloadLink.download = `page_${pageNumber}.png`;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();

        // Revoke the URL object
        URL.revokeObjectURL(downloadLink.href);

        console.log(`Page ${pageNumber} download completed.`);
    });
}


// Call the function to download pages 1 to 40
downloadPages(1, 40);

#include <stdint.h>

/**
 * Common Data Types
 */
typedef uint8_t  BYTE;
typedef uint32_t DWORD;
typedef int32_t  LONG;
typedef uint16_t WORD;

/**
 * BITMAPFILEHEADER
 */
#pragma pack(push, 1)  // Ensure no padding between fields
typedef struct {
    WORD   bfType;      // File type, must be 'BM' (0x4D42)
    DWORD  bfSize;      // Size of the file in bytes
    WORD   bfReserved1; // Reserved, must be 0
    WORD   bfReserved2; // Reserved, must be 0
    DWORD  bfOffBits;   // Offset to start of Pixel Data
} BITMAPFILEHEADER;
#pragma pack(pop)  // Restore previous packing alignment

/**
 * BITMAPINFOHEADER
 */
#pragma pack(push, 1)
typedef struct {
    DWORD  biSize;          // Size of this header (40 bytes)
    LONG   biWidth;         // Image width in pixels
    LONG   biHeight;        // Image height in pixels
    WORD   biPlanes;        // Number of color planes (must be 1)
    WORD   biBitCount;      // Number of bits per pixel (e.g., 24 for RGB)
    DWORD  biCompression;   // Compression type (0 for no compression)
    DWORD  biSizeImage;     // Image size (can be 0 for uncompressed images)
    LONG   biXPelsPerMeter;  // Horizontal resolution (pixels per meter)
    LONG   biYPelsPerMeter;  // Vertical resolution (pixels per meter)
    DWORD  biClrUsed;       // Number of colors in the color table
    DWORD  biClrImportant;   // Number of important colors
} BITMAPINFOHEADER;
#pragma pack(pop)  // Restore previous packing alignment

/**
 * RGBTRIPLE
 */
typedef struct __attribute__((__packed__)) {
    BYTE  rgbtBlue;
    BYTE  rgbtGreen;
    BYTE  rgbtRed;
} RGBTRIPLE;

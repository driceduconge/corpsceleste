<?php

function getXmpData($filename, $chunkSize)
{
    if (!is_int($chunkSize)) {
        throw new RuntimeException('Expected integer value for argument #2 (chunkSize)');
    }

    if ($chunkSize < 12) {
        throw new RuntimeException('Chunk size cannot be less than 12 argument #2 (chunkSize)');
    }

    if (($file_pointer = fopen($filename, 'r')) === FALSE) {
        throw new RuntimeException('Could not open file for reading');
    }

    $startTag = '<x:xmpmeta';
    $endTag = '</x:xmpmeta>';
    $buffer = NULL;
    $hasXmp = FALSE;

    while (($chunk = fread($file_pointer, $chunkSize)) !== FALSE) {

        if ($chunk === "") {
            break;
        }

        $buffer .= $chunk;
        $startPosition = strpos($buffer, $startTag);
        $endPosition = strpos($buffer, $endTag);

        if ($startPosition !== FALSE && $endPosition !== FALSE) {
            $buffer = substr($buffer, $startPosition, $endPosition - $startPosition + 12);
            $hasXmp = TRUE;
            break;
        } elseif ($startPosition !== FALSE) {
            $buffer = substr($buffer, $startPosition);
            $hasXmp = TRUE;
        } elseif (strlen($buffer) > (strlen($startTag) * 2)) {
            $buffer = substr($buffer, strlen($startTag));
        }
    }

    fclose($file_pointer);
    return ($hasXmp) ? $buffer : NULL;
}

class XmlToJson {
public function Parse ($url) {
		$fileContents= file_get_contents($url);
		$fileContents = str_replace(array("\n", "\r", "\t"), '', $fileContents);
		$fileContents = trim(str_replace('"', "'", $fileContents));
		$simpleXml = simplexml_load_string($fileContents);
		$json = json_encode($simpleXml);
		return $json;
	}
}

$xmlStr = getXmpData("STRASBOURG_GOVIGNON_Lea_00.tif", 50000);
// $xml  = simplexml_load_string( $xmlStr );
// $json = json_encode($xmlStr);
// $array = json_decode($json,TRUE);

// print_r( XmlToJson::parse("xmp-data.xml") );

$image = "STRASBOURG_GOVIGNON_Lea_00.tif";

print_r("\n");

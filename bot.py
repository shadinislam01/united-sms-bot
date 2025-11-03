<?php
// error_reporting(E_ALL);
// ini_set('display_errors', 1);

// ===================================================================
// --- Configuration ---
// ===================================================================
define('BOT_NAME', "Latest Otp");
define('PANEL_USERNAME', "একাউন্ট ইউজারনেম");
define('PANEL_PASSWORD', "একাউন্ট পাসওয়ার্ড");
define('DB_FILE', __DIR__ . "/sms_database.db");
define('COOKIE_FILE', __DIR__ . "/cookie.txt");
define('TELEGRAM_BOT_TOKEN', "7776620484:AAFjTHOC37XSENynllLMzrzrBZkqpcAwCQI");
define('DEFAULT_GROUP_CHAT_ID', "-1001846882115");
define('DEVELOPER_TELEGRAM_URL', "https://t.me/md_shadhin12");
define('DETECTLANGUAGE_API_KEY', "লাউ্গুয়েজ এপিআই");
define('BASE_URL',"http://54.37.83.141/ints");
define('LOGIN_PAGE_URL', BASE_URL . "/");
define('SMS_HTML_PAGE_URL', BASE_URL . "/agent/SMSCDRReports");
define('API_URL', BASE_URL . "/agent/res/data_smscdr.php");

// ===================================================================
// --- Data for Formatting ---
// ===================================================================
const COUNTRY_CODES = [
    '1' => ['USA/Canada', '🇺🇸'], '7' => ['Russia/Kazakhstan', '🇷🇺'], '20' => ['Egypt', '🇪🇬'], '27' => ['South Africa', '🇿🇦'], '30' => ['Greece', '🇬🇷'],
    '31' => ['Netherlands', '🇳🇱'], '32' => ['Belgium', '🇧🇪'], '33' => ['France', '🇫🇷'], '34' => ['Spain', '🇪🇸'], '36' => ['Hungary', '🇭🇺'],
    '39' => ['Italy', '🇮🇹'], '40' => ['Romania', '🇷🇴'], '41' => ['Switzerland', '🇨🇭'], '43' => ['Austria', '🇦🇹'], '44' => ['United Kingdom', '🇬🇧'],
    '45' => ['Denmark', '🇩🇰'], '46' => ['Sweden', '🇸🇪'], '47' => ['Norway', '🇳🇴'], '48' => ['Poland', '🇵🇱'], '49' => ['Germany', '🇩🇪'],
    '51' => ['Peru', '🇵🇪'], '52' => ['Mexico', '🇲🇽'], '53' => ['Cuba', '🇨🇺'], '54' => ['Argentina', '🇦🇷'], '55' => ['Brazil', '🇧🇷'],
    '56' => ['Chile', '🇨🇱'], '57' => ['Colombia', '🇨🇴'], '58' => ['Venezuela', '🇻🇪'], '60' => ['Malaysia', '🇲🇾'], '61' => ['Australia', '🇦🇺'],
    '62' => ['Indonesia', '🇮🇩'], '63' => ['Philippines', '🇵🇭'], '64' => ['New Zealand', '🇳🇿'], '65' => ['Singapore', '🇸🇬'], '66' => ['Thailand', '🇹🇭'],
    '81' => ['Japan', '🇯🇵'], '82' => ['South Korea', '🇰🇷'], '84' => ['Vietnam', '🇻🇳'], '86' => ['China', '🇨🇳'], '90' => ['Turkey', '🇹🇷'],
    '91' => ['India', '🇮🇳'], '92' => ['Pakistan', '🇵🇰'], '93' => ['Afghanistan', '🇦🇫'], '94' => ['Sri Lanka', '🇱🇰'], '95' => ['Myanmar', '🇲🇲'],
    '98' => ['Iran', '🇮🇷'], '211' => ['South Sudan', '🇸🇸'], '212' => ['Morocco', '🇲🇦'], '213' => ['Algeria', '🇩🇿'], '216' => ['Tunisia', '🇹🇳'],
    '218' => ['Libya', '🇱🇾'], '220' => ['Gambia', '🇬🇲'], '221' => ['Senegal', '🇸🇳'], '222' => ['Mauritania', '🇲🇷'], '223' => ['Mali', '🇲🇱'],
    '224' => ['Guinea', '🇬🇳'], '225' => ["Côte d'Ivoire", '🇨🇮'], '226' => ['Burkina Faso', '🇧🇫'], '227' => ['Niger', '🇳🇪'], '228' => ['Togo', '🇹🇬'],
    '229' => ['Benin', '🇧🇯'], '230' => ['Mauritius', '🇲🇺'], '231' => ['Liberia', '🇱🇷'], '232' => ['Sierra Leone', '🇸🇱'], '233' => ['Ghana', '🇬🇭'],
    '234' => ['Nigeria', '🇳🇬'], '235' => ['Chad', '🇹🇩'], '236' => ['Central African Republic', '🇨🇫'], '237' => ['Cameroon', '🇨🇲'], '238' => ['Cape Verde', '🇨🇻'],
    '239' => ['Sao Tome & Principe', '🇸🇹'], '240' => ['Equatorial Guinea', '🇬🇶'], '241' => ['Gabon', '🇬🇦'], '242' => ['Congo - Brazzaville', '🇨🇬'], '243' => ['Congo - Kinshasa', '🇨🇩'],
    '244' => ['Angola', '🇦🇴'], '245' => ['Guinea-Bissau', '🇬🇼'], '246' => ['British Indian Ocean Territory', '🇮🇴'], '248' => ['Seychelles', '🇸🇨'], '249' => ['Sudan', '🇸🇩'],
    '250' => ['Rwanda', '🇷🇼'], '251' => ['Ethiopia', '🇪🇹'], '252' => ['Somalia', '🇸🇴'], '253' => ['Djibouti', '🇩🇯'], '254' => ['Kenya', '🇰🇪'],
    '255' => ['Tanzania', '🇹🇿'], '256' => ['Uganda', '🇺🇬'], '257' => ['Burundi', '🇧🇮'], '258' => ['Mozambique', '🇲🇿'], '260' => ['Zambia', '🇿🇲'],
    '261' => ['Madagascar', '🇲🇬'], '262' => ['Réunion', '🇷🇪'], '263' => ['Zimbabwe', '🇿🇼'], '264' => ['Namibia', '🇳🇦'], '265' => ['Malawi', '🇲🇼'],
    '266' => ['Lesotho', '🇱🇸'], '267' => ['Botswana', '🇧🇼'], '268' => ['Eswatini', '🇸🇿'], '269' => ['Comoros', '🇰🇲'], '290' => ['Saint Helena', '🇸🇭'],
    '291' => ['Eritrea', '🇪🇷'], '297' => ['Aruba', '🇦🇼'], '298' => ['Faroe Islands', '🇫🇴'], '299' => ['Greenland', '🇬🇱'], '350' => ['Gibraltar', '🇬🇮'],
    '351' => ['Portugal', '🇵🇹'], '352' => ['Luxembourg', '🇱🇺'], '353' => ['Ireland', '🇮🇪'], '354' => ['Iceland', '🇮🇸'], '355' => ['Albania', '🇦🇱'],
    '356' => ['Malta', '🇲🇹'], '357' => ['Cyprus', '🇨🇾'], '358' => ['Finland', '🇫🇮'], '359' => ['Bulgaria', '🇧🇬'], '370' => ['Lithuania', '🇱🇹'],
    '371' => ['Latvia', '🇱🇻'], '372' => ['Estonia', '🇪🇪'], '373' => ['Moldova', '🇲🇩'], '374' => ['Armenia', '🇦🇲'], '375' => ['Belarus', '🇧🇾'],
    '376' => ['Andorra', '🇦🇩'], '377' => ['Monaco', '🇲🇨'], '378' => ['San Marino', '🇸🇲'], '379' => ['Vatican City', '🇻🇦'], '380' => ['Ukraine', '🇺🇦'],
    '381' => ['Serbia', '🇷🇸'], '382' => ['Montenegro', '🇲🇪'], '383' => ['Kosovo', '🇽🇰'], '385' => ['Croatia', '🇭🇷'], '386' => ['Slovenia', '🇸🇮'],
    '387' => ['Bosnia & Herzegovina', '🇧🇦'], '389' => ['North Macedonia', '🇲🇰'], '420' => ['Czech Republic', '🇨🇿'], '421' => ['Slovakia', '🇸🇰'], '423' => ['Liechtenstein', '🇱🇮'],
    '500' => ['Falkland Islands', '🇫🇰'], '501' => ['Belize', '🇧🇿'], '502' => ['Guatemala', '🇬🇹'], '503' => ['El Salvador', '🇸🇻'], '504' => ['Honduras', '🇭🇳'],
    '505' => ['Nicaragua', '🇳🇮'], '506' => ['Costa Rica', '🇨🇷'], '507' => ['Panama', '🇵🇦'], '508' => ['St. Pierre & Miquelon', '🇵🇲'], '509' => ['Haiti', '🇭🇹'],
    '590' => ['Guadeloupe', '🇬🇵'], '591' => ['Bolivia', '🇧🇴'], '592' => ['Guyana', '🇬🇾'], '593' => ['Ecuador', '🇪🇨'], '594' => ['French Guiana', '🇬🇫'],
    '595' => ['Paraguay', '🇵🇾'], '596' => ['Martinique', '🇲🇶'], '597' => ['Suriname', '🇸🇷'], '598' => ['Uruguay', '🇺🇾'], '599' => ['Curaçao', '🇨🇼'],
    '670' => ['Timor-Leste', '🇹🇱'], '672' => ['Norfolk Island', '🇳🇫'], '673' => ['Brunei', '🇧🇳'], '674' => ['Nauru', '🇳🇷'], '675' => ['Papua New Guinea', '🇵🇬'],
    '676' => ['Tonga', '🇹🇴'], '677' => ['Solomon Islands', '🇸🇧'], '678' => ['Vanuatu', '🇻🇺'], '679' => ['Fiji', '🇫🇯'], '680' => ['Palau', '🇵🇼'],
    '681' => ['Wallis & Futuna', '🇼🇫'], '682' => ['Cook Islands', '🇨🇰'], '683' => ['Niue', '🇳🇺'], '685' => ['Samoa', '🇼🇸'], '686' => ['Kiribati', '🇰🇮'],
    '687' => ['New Caledonia', '🇳🇨'], '688' => ['Tuvalu', '🇹🇻'], '689' => ['French Polynesia', '🇵🇫'], '690' => ['Tokelau', '🇹🇰'], '691' => ['Micronesia', '🇫🇲'],
    '692' => ['Marshall Islands', '🇲🇭'], '850' => ['North Korea', '🇰🇵'], '852' => ['Hong Kong', '🇭🇰'], '853' => ['Macau', '🇲🇴'], '855' => ['Cambodia', '🇰🇭'],
    '856' => ['Laos', '🇱🇦'], '880' => ['Bangladesh', '🇧🇩'], '886' => ['Taiwan', '🇹🇼'], '960' => ['Maldives', '🇲🇻'], '961' => ['Lebanon', '🇱🇧'],
    '962' => ['Jordan', '🇯🇴'], '963' => ['Syria', '🇸🇾'], '964' => ['Iraq', '🇮🇶'], '965' => ['Kuwait', '🇰🇼'], '966' => ['Saudi Arabia', '🇸🇦'],
    '967' => ['Yemen', '🇾🇪'], '968' => ['Oman', '🇴🇲'], '970' => ['Palestine', '🇵🇸'], '971' => ['United Arab Emirates', '🇦🇪'], '972' => ['Israel', '🇮🇱'],
    '973' => ['Bahrain', '🇧🇭'], '974' => ['Qatar', '🇶🇦'], '975' => ['Bhutan', '🇧🇹'], '976' => ['Mongolia', '🇲🇳'], '977' => ['Nepal', '🇳🇵'],
    '992' => ['Tajikistan', '🇹🇯'], '993' => ['Turkmenistan', '🇹🇲'], '994' => ['Azerbaijan', '🇦🇿'], '995' => ['Georgia', '🇬🇪'], '996' => ['Kyrgyzstan', '🇰🇬'],
    '998' => ['Uzbekistan', '🇺🇿']
];
const LANGUAGE_MAP = [
    'af' => 'Afrikaans', 'ak' => 'Akan', 'am' => 'Amharic', 'ar' => 'Arabic', 'as' => 'Assamese', 'ay' => 'Aymara', 'az' => 'Azerbaijani', 'be' => 'Belarusian',
    'bg' => 'Bulgarian', 'bho' => 'Bhojpuri', 'bm' => 'Bambara', 'bn' => 'Bengali', 'bs' => 'Bosnian', 'ca' => 'Catalan', 'ceb' => 'Cebuano', 'ckb' => 'Central Kurdish',
    'co' => 'Corsican', 'cs' => 'Czech', 'cy' => 'Welsh', 'da' => 'Danish', 'de' => 'German', 'doi' => 'Dogri', 'dv' => 'Dhivehi', 'ee' => 'Ewe', 'el' => 'Greek',
    'en' => 'English', 'eo' => 'Esperanto', 'es' => 'Spanish', 'et' => 'Estonian', 'eu' => 'Basque', 'fa' => 'Persian', 'fi' => 'Finnish', 'fr' => 'French',
    'fy' => 'Frisian', 'ga' => 'Irish', 'gd' => 'Scottish Gaelic', 'gl' => 'Galician', 'gn' => 'Guarani', 'gom' => 'Goan Konkani', 'gu' => 'Gujarati',
    'ha' => 'Hausa', 'haw' => 'Hawaiian', 'he' => 'Hebrew', 'hi' => 'Hindi', 'hmn' => 'Hmong', 'hr' => 'Croatian', 'ht' => 'Haitian Creole', 'hu' => 'Hungarian',
    'hy' => 'Armenian', 'id' => 'Indonesian', 'ig' => 'Igbo', 'ilo' => 'Iloko', 'is' => 'Icelandic', 'it' => 'Italian', 'ja' => 'Japanese', 'jv' => 'Javanese',
    'ka' => 'Georgian', 'kk' => 'Kazakh', 'km' => 'Khmer', 'kn' => 'Kannada', 'ko' => 'Korean', 'kri' => 'Krio', 'ku' => 'Kurdish', 'ky' => 'Kyrgyz',
    'la' => 'Latin', 'lb' => 'Luxembourgish', 'lg' => 'Ganda', 'ln' => 'Lingala', 'lo' => 'Lao', 'lt' => 'Lithuanian', 'lus' => 'Mizo', 'lv' => 'Latvian',
    'mai' => 'Maithili', 'mg' => 'Malagasy', 'mi' => 'Maori', 'mk' => 'Macedonian', 'ml' => 'Malayalam', 'mn' => 'Mongolian', 'mni-Mtei' => 'Meiteilon',
    'mr' => 'Marathi', 'ms' => 'Malay', 'mt' => 'Maltese', 'my' => 'Myanmar', 'ne' => 'Nepali', 'nl' => 'Dutch', 'no' => 'Norwegian', 'nso' => 'Sepedi',
    'ny' => 'Nyanja', 'om' => 'Oromo', 'or' => 'Oriya', 'pa' => 'Punjabi', 'pl' => 'Polish', 'ps' => 'Pashto', 'pt' => 'Portuguese', 'qu' => 'Quechua',
    'ro' => 'Romanian', 'ru' => 'Russian', 'rw' => 'Kinyarwanda', 'sa' => 'Sanskrit', 'sd' => 'Sindhi', 'si' => 'Sinhala', 'sk' => 'Slovak', 'sl' => 'Slovenian',
    'sm' => 'Samoan', 'sn' => 'Shona', 'so' => 'Somali', 'sq' => 'Albanian', 'sr' => 'Serbian', 'st' => 'Sesotho', 'su' => 'Sundanese', 'sv' => 'Swedish',
    'sw' => 'Swahili', 'ta' => 'Tamil', 'te' => 'Telugu', 'tg' => 'Tajik', 'th' => 'Thai', 'ti' => 'Tigrinya', 'tk' => 'Turkmen', 'tl' => 'Filipino',
    'tr' => 'Turkish', 'ts' => 'Tsonga', 'ug' => 'Uyghur', 'uk' => 'Ukrainian', 'ur' => 'Urdu', 'uz' => 'Uzbek', 'vi' => 'Vietnamese', 'xh' => 'Xhosa',
    'yi' => 'Yiddish', 'yo' => 'Yoruba', 'zh' => 'Chinese', 'zu' => 'Zulu'
];

// ===================================================================
// --- Functions ---
// ===================================================================
function detect_language($text) {
    if (!defined('DETECTLANGUAGE_API_KEY') || empty(DETECTLANGUAGE_API_KEY)) return "Unknown";
    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => "https://ws.detectlanguage.com/0.2/detect",
        CURLOPT_HTTPHEADER => ["Content-Type: application/json", "Authorization: Bearer " . DETECTLANGUAGE_API_KEY],
        CURLOPT_POSTFIELDS => json_encode(['q' => $text]),
        CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 4
    ]);
    $response = curl_exec($ch);
    curl_close($ch);
    if ($response) {
        $data = json_decode($response, true);
        if (isset($data['data']['detections'][0]['language'])) {
            $lang_code = $data['data']['detections'][0]['language'];
            return LANGUAGE_MAP[$lang_code] ?? ucfirst($lang_code);
        }
    }
    return "Unknown";
}

function mask_number($number) {
    return strlen($number) > 7 ? substr($number, 0, 3) . '****' . substr($number, -4) : $number;
}

function get_country_info($phone_number) {
    for ($i = 4; $i > 0; $i--) {
        $prefix = substr($phone_number, 0, $i);
        if (isset(COUNTRY_CODES[$prefix])) return COUNTRY_CODES[$prefix];
    }
    return ['Unknown', '🌍'];
}

function format_telegram_message($recipient_number, $sender_name, $message, $otp, $sms_time) {
    list($country_name, $country_flag) = get_country_info($recipient_number);
    $service_name = strtoupper($sender_name);
    $masked_number = mask_number($recipient_number);
    $detected_language = detect_language($message);
    return "✨ Team SHADIN ISLAM ✨\n\n"
         . "⏰ Time: {$sms_time}\n"
         . "📞 Number: {$masked_number}\n"
         . "🛠 Service: {$service_name}\n"
         . "🌍 Country: {$country_flag} {$country_name}\n"
         . "🗣️ Language: {$detected_language}\n\n"
         . "🔑 OTP Code: {$otp}\n\n"
         . '✅ BOT MAKE: <a href="' . DEVELOPER_TELEGRAM_URL . '">SHADIN ISLAM</a>';
}

function send_telegram_message($chat_id, $text) {
    $url = "https://api.telegram.org/bot" . TELEGRAM_BOT_TOKEN . "/sendMessage";
    $payload = ['chat_id' => $chat_id, 'text' => $text, 'parse_mode' => 'HTML', 'disable_web_page_preview' => true];
    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url, CURLOPT_POST => true, CURLOPT_POSTFIELDS => json_encode($payload),
        CURLOPT_HTTPHEADER => ['Content-Type: application/json'], CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 10
    ]);
    curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return $http_code === 200;
}

function get_db_connection() {
    static $pdo = null;
    if ($pdo === null) {
        try {
            $pdo = new PDO("sqlite:" . DB_FILE);
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $pdo->exec('CREATE TABLE IF NOT EXISTS reported_sms (hash TEXT PRIMARY KEY)');
        } catch (PDOException $e) { die("[!!!] DATABASE ERROR: " . $e->getMessage()); }
    }
    return $pdo;
}

function is_sms_reported($hash) {
    $stmt = get_db_connection()->prepare("SELECT 1 FROM reported_sms WHERE hash = ?");
    $stmt->execute([$hash]);
    return $stmt->fetchColumn() !== false;
}

function add_sms_to_reported_db($hash) {
    try {
        $stmt = get_db_connection()->prepare("INSERT INTO reported_sms (hash) VALUES (?)");
        $stmt->execute([$hash]);
    } catch (PDOException $e) { /* Hash already exists */ }
}

function solve_math_captcha($captcha_text) {
    if (preg_match('/(\d+)\s*([+*])\s*(\d+)/', $captcha_text, $matches)) {
        return $matches[2] === '+' ? ((int)$matches[1] + (int)$matches[3]) : ((int)$matches[1] * (int)$matches[3]);
    }
    return null;
}

// OPTIMIZED: Function to perform login only once.
function do_login($ch) {
    echo "Attempting to login...\n";
    curl_setopt($ch, CURLOPT_URL, LOGIN_PAGE_URL);
    $login_page_html = curl_exec($ch);
    $doc = new DOMDocument();
    @$doc->loadHTML($login_page_html);
    $xpath = new DOMXPath($doc);
    $form = $xpath->query('//form')->item(0);
    if (!$form) { return false; }
    $post_url = $form->getAttribute('action');
    if (strpos($post_url, 'http') !== 0) { $post_url = BASE_URL . '/' . ltrim($post_url, '/'); }
    $payload = [];
    $inputs = $xpath->query('.//input', $form);
    foreach ($inputs as $input) {
        $name = $input->getAttribute('name'); $value = $input->getAttribute('value');
        $placeholder = strtolower($input->getAttribute('placeholder'));
        if (!$name) continue;
        if (strpos($placeholder, 'user') !== false) { $payload[$name] = PANEL_USERNAME; }
        elseif (strpos($placeholder, 'pass') !== false) { $payload[$name] = PANEL_PASSWORD; }
        elseif (strpos($placeholder, 'ans') !== false) {
            $captcha_text_node = $xpath->query("//*[contains(text(), 'What is')]")->item(0);
            if (!$captcha_text_node) { return false; }
            $payload[$name] = solve_math_captcha($captcha_text_node->nodeValue);
        } else { $payload[$name] = $value; }
    }
    curl_setopt($ch, CURLOPT_URL, $post_url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_REFERER, LOGIN_PAGE_URL);
    $response_html = curl_exec($ch);
    if (strpos($response_html, 'Logout') === false) {
        echo "Login failed!\n";
        return false;
    }
    echo "Login successful!\n";
    return true;
}

// OPTIMIZED: Function to only fetch SMS data, assuming login is done.
function fetch_and_process_sms($ch) {
    echo "--- Fetching SMS at " . date('H:i:s') . "\n";
    $date_to = date('Y-m-d H:i:s');
    $date_from = date('Y-m-d H:i:s', strtotime('-1 day'));
    $params = http_build_query(['fdate1' => $date_from, 'fdate2' => $date_to]);
    curl_setopt($ch, CURLOPT_URL, API_URL . '?' . $params);
    curl_setopt($ch, CURLOPT_POST, false);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Accept: application/json, text/javascript, */*; q=0.01", "X-Requested-With: XMLHttpRequest"]);
    curl_setopt($ch, CURLOPT_REFERER, SMS_HTML_PAGE_URL);
    $api_response = curl_exec($ch);
    $json_data = json_decode($api_response, true);
    if (!$json_data || !isset($json_data['aaData']) || !is_array($json_data['aaData'])) {
        echo "[!] Invalid API response format.\n";
        return;
    }
    $sms_list = array_reverse($json_data['aaData']);
    $new_sms_count = 0;
    foreach ($sms_list as $sms_data) {
        if (count($sms_data) > 5) {
            $dt = (string)$sms_data[0]; $rc = (string)$sms_data[2];
            $sn = (string)$sms_data[3]; $msg = (string)$sms_data[5];
            if (empty($msg) || empty($rc) || trim($rc) === '0' || strlen(trim($rc)) < 5) continue;
            $hash = md5("{$dt}-{$rc}-{$msg}");
            if (!is_sms_reported($hash)) {
                $new_sms_count++;
                preg_match('/\b(\d{3}[-\s]\d{3})\b|\b(\d{4,8})\b/', $msg, $otp_match);
                $otp = $otp_match[0] ?? "N/A";
                $notification_message = format_telegram_message($rc, $sn, $msg, $otp, $dt);
                if (send_telegram_message(DEFAULT_GROUP_CHAT_ID, $notification_message)) {
                    add_sms_to_reported_db($hash);
                }
            }
        }
    }
    if ($new_sms_count > 0) {
        echo "--- Found and sent {$new_sms_count} new SMS.\n";
    }
}

// ===================================================================
// --- Main Execution Logic (Optimized Looping) ---
// ===================================================================
echo "====================================================\n";
echo "--- Fast OTP Bot Initialized at: " . date('Y-m-d H:i:s') . " ---\n";
echo "====================================================\n\n";

// Initialize cURL handle to be reused
$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    CURLOPT_COOKIEJAR => COOKIE_FILE, CURLOPT_COOKIEFILE => COOKIE_FILE,
    CURLOPT_CONNECTTIMEOUT => 5, CURLOPT_TIMEOUT => 10
]);

// Step 1: Login only ONCE.
if (do_login($ch)) {
    // Step 2: Loop the fetching process.
    echo "\nStarting 10-second polling cycle...\n";
    for ($i = 0; $i < 6; $i++) {
        fetch_and_process_sms($ch);
        
        // Wait for 10 seconds before the next check, but not after the last one.
        if ($i < 5) {
            sleep(10);
        }
    }
}

// Clean up
curl_close($ch);

echo "\n====================================================\n";
echo "--- Script finished its 1-minute cycle. ---\n";
echo "====================================================\n";
?>

/*
  TRNG PROJECT - ARDUINO SOFTWARE
  2021
*/

void setup() {
  Serial.begin(115200);
  DDRC = 0x00; // reg C all input
  DDRB = 0xFF; // reg B all output, we will only use B5
               // for some debugging via on board LED
  // show that it's alive
  blinky(3);
  delay(120);
  blinky(3);
}

// blinks N times. is there for debug/demo purposes
void blinky(unsigned char n)
{
  for (unsigned char t = 0; t < n; t++)
 {
   PORTB = 0xFF;
   delay(60);
   PORTB = 0x00;
   delay(60);
 } 
}

// resets the connection - this resolves the locked port bug
void softReset()
{
  blinky(1);
  delay(50);
  Serial.end();
  delay(500);
  Serial.begin(115200);
  blinky(2);
}

// function for accumulating 1 byte worth of uncertainty
char getByteData()
{
  char out = 0,
       temp = 0;    
  for (unsigned char counter = 0; counter < 8; counter++)
  {
    out = out << 1;
    temp = (PINC >> 5) & 0x01;
    out |= temp;
    
    // slow noise compensation - to be removed when the circuitry gets upgraded
    for (int a = 0; a < 128; a++)
    {
     __asm__ __volatile__ ("nop\n\t");
    }  
  }
  return out;
}

// generates a random byte by getting 2 uncertainty bytes and XORing them for
// even more advanced effect
char getRandomByte()
{
  char byte1 = getByteData();
  char byte2 = getByteData();
  char out = byte1 ^ byte2;
  return out;
}

// the 'awit for command' loop
char opt = '0';
void loop() 
{
  // READ OPTION
  
  if (Serial.available() > 0) 
  {
    opt = Serial.read();
  }
  
  // D(isconnects) the connection
  if (opt == 'D')
  {
    softReset();
  }
  
  // send a single random B(yte)
  else if (opt == 'B')
  {
    char out = getRandomByte();
    Serial.print(out); 
  }
  
  // S(tream) UNTIL E(nough)
  else if (opt == 'S')
  {
    char temp = 0,
         byte1 = 0,
         byte2 = 0;
    
    while (true)
    {
      // E(nough) breakout sequence
      if (Serial.available() > 0) 
      {
        if (Serial.read() == 'E')
          break;
      }
      char out = getRandomByte();
      Serial.print(out);
    }
  }

  // nullify the option if it was not zero
  if (opt != '0')
    opt = '0';
}


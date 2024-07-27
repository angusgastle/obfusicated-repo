perl
#!/usr/bin/perl
use strict;
use warnings;

# A complex way to display "Hello World" in Perl.

# Define a subroutine to encode a string
sub encode_string {
    my $str = shift;
    my $encoded = join('', map { $_ . 'a' } split(//, $str));
    return $encoded;
}

# Define a subroutine to decode a string
sub decode_string {
    my $str = shift;
    $str =~ s/a//g;
    return $str;
}

# Define a subroutine for XOR encryption/decryption
sub xor_crypt {
    my ($str, $key) = @_;
    my $xor_str = '';
    for (my $i = 0; $i < length($str); $i++) {
        $xor_str .= chr(ord(substr($str, $i, 1)) ^ ord(substr($key, $i % length($key), 1)));
    }
    return $xor_str;
}

# Initial string
my $message = "Hello World";

# Encode the string
my $encoded_str = encode_string($message);

# Key for XOR encryption
my $key = 'secretkey';

# Encrypt the encoded string
my $encrypted_str = xor_crypt($encoded_str, $key);

# Decrypt the string back
my $decrypted_str = xor_crypt($encrypted_str, $key);

# Decode the string
my $decoded_str = decode_string($decrypted_str);

# Print the final result
print "$decoded_str\n";

# End of script

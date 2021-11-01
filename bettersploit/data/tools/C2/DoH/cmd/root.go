package cmd

import (
	"crypto/tls"
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"strings"
	"time"

	"github.com/sensepost/godoh/dnsclient"

	log "github.com/sirupsen/logrus"

	"github.com/spf13/cobra"
)

// Version is the version of godoh
var Version string

var dnsDomain string
var dnsProviderName string
var dnsProvider dnsclient.Client
var validateSSL bool

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "godoh",
	Short: "A DNS (over-HTTPS) C2",
	Long: `A DNS (over-HTTPS) C2
    Version: ` + Version + `
	By @leonjza from @sensepost`,
	Run: func(cmd *cobra.Command, args []string) {

		// by default, start in agent mode
		if len(args) == 0 {
			agentCmd.Run(cmd, args)
			os.Exit(0)
		}
	},
}

// Execute adds all child commands to the root command and sets flags appropriately.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func init() {
	cobra.OnInitialize(validateDNSProvider)
	cobra.OnInitialize(validateDNSDomain)
	cobra.OnInitialize(seedRand)
	cobra.OnInitialize(configureSSLValidation)

	// if the DNS domain was configured at compile time, remove the flag
	if dnsDomain == "" {
		rootCmd.PersistentFlags().StringVarP(&dnsDomain,
			"domain", "d", "", "DNS Domain to use. (ie: example.com)")
	}

	rootCmd.PersistentFlags().StringVarP(&dnsProviderName,
		"provider", "p", "google",
		"Preferred DNS provider to use. [possible: googlefront, google, cloudflare, quad9, raw]")
	rootCmd.PersistentFlags().BoolVarP(&validateSSL,
		"validate-certificate", "K", false, "Validate DoH provider SSL certificates")
}

func seedRand() {
	rand.Seed(time.Now().UTC().UnixNano())
}

func validateDNSDomain() {
	if dnsDomain == "" {
		log.Fatalf("A DNS domain to use is required.")
	}

	if strings.HasPrefix(dnsDomain, ".") {
		log.Fatalf("The DNS domain should be the base FQDN (without a leading dot).")
	}

	log.Infof("Using %s as DNS domain\n", dnsDomain)
}

func validateDNSProvider() {
	switch dnsProviderName {
	case "googlefront":
		log.Warn(`WARNING: Domain fronting dns.google.com via www.google.com no longer works. ` +
			`A redirect to dns.google.com will be returned. See: https://twitter.com/leonjza/status/1187002742553923584`)
		dnsProvider = dnsclient.NewGoogleFrontDNS()
		break
	case "google":
		dnsProvider = dnsclient.NewGoogleDNS()
		break
	case "cloudflare":
		dnsProvider = dnsclient.NewCloudFlareDNS()
		break
	case "quad9":
		dnsProvider = dnsclient.NewQuad9DNS()
		break
	case "raw":
		dnsProvider = dnsclient.NewRawDNS()
		break
	default:
		log.Fatalf("DNS provider `%s` is not valid.\n", dnsProviderName)
	}

	log.Infof("Using `%s` as preferred provider\n", dnsProviderName)
}

func configureSSLValidation() {
	if !validateSSL {
		http.DefaultTransport.(*http.Transport).TLSClientConfig = &tls.Config{InsecureSkipVerify: true}
	}
}

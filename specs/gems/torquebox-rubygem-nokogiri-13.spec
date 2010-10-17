%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     nokogiri
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-nokogiri-13
Version: 1.4.3.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Nokogiri (&#37624;) is an HTML, XML, SAX, and Reader parser
URL: http://nokogiri.org
Source0: http://rubygems.org/gems/nokogiri-1.4.3.1-java.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(weakling) >= 0.0.3

%description

Nokogiri (&#37624;) is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.

XML is like violence - if it doesn&#8217;t solve your problems, you are not using
enough of it.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/nokogiri-1.4.3.1-java/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform java %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/nokogiri-1.4.3.1-java/
%{gem_dir}/cache/nokogiri-1.4.3.1-java.gem
%{gem_dir}/specifications/nokogiri-1.4.3.1-java.gemspec
%doc %{gem_dir}/doc/nokogiri-1.4.3.1-java

%changelog


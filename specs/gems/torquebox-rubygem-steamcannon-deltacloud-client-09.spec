%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     steamcannon-deltacloud-client
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-steamcannon-deltacloud-client-09
Version: 0.0.9.7.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Deltacloud REST Client
URL: http://www.deltacloud.org
Source0: http://rubygems.org/gems/steamcannon-deltacloud-client-0.0.9.7.2-java.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(rest-client) >= 1.4.2
Requires: %{tree_prefix}rubygem(nokogiri) >= 1.5.0.beta.2

%description

Deltacloud REST Client for API

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/steamcannon-deltacloud-client-0.0.9.7.2-java/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform java %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/steamcannon-deltacloud-client-0.0.9.7.2-java/
%{gem_dir}/cache/steamcannon-deltacloud-client-0.0.9.7.2-java.gem
%{gem_dir}/specifications/steamcannon-deltacloud-client-0.0.9.7.2-java.gemspec
%doc %{gem_dir}/doc/steamcannon-deltacloud-client-0.0.9.7.2-java

%changelog


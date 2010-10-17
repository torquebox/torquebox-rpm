%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     paperclip
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-paperclip-23
Version: 2.3.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: File attachments as attributes for ActiveRecord
URL: http://www.thoughtbot.com/projects/paperclip
Source0: http://rubygems.org/gems/paperclip-2.3.3.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(activerecord) >= 0
Requires: %{tree_prefix}rubygem(activesupport) >= 0

%description

Easy upload management for ActiveRecord

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/paperclip-2.3.3/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/paperclip-2.3.3/
%{gem_dir}/cache/paperclip-2.3.3.gem
%{gem_dir}/specifications/paperclip-2.3.3.gemspec
%doc %{gem_dir}/doc/paperclip-2.3.3

%changelog

